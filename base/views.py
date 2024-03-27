from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import List
from django.contrib.auth.models import User
from .forms import ListForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .serializers import ListSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

def loginPage(request):
    page='login'
    if request.method == 'POST':
    
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'user doesn\'t exist!')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password is incorrect')

    context={'page':page}
    return render(request,'base/login_signup.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    page='register'
    form = UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"an error occured during registration")
    context={'form':form,'page':page}
    return render(request,'base/login_signup.html',context)

def home(request):
    Lists=List.objects.all()

    listcount=Lists.count()
    context={'Lists':Lists,'listcount':listcount}
    return render(request,'base/home.html',context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addtask(request):
    serializer = ListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return redirect('home')
    else:
        return redirect('login')




def deletetask(request,pk):
    llist=List.objects.get(id=pk)
    
    if request.method == 'POST':
        llist.delete()
        return redirect('home')

    context={'obj':llist}
    return render(request,'base/delete.html',context)