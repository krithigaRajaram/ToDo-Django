from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import List
from django.contrib.auth.models import User
from .forms import ListForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

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
    return redirect('home')

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

@login_required(login_url='login')
def addtask(request):
    form=ListForm()
    if request.method == "POST":
        form=ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'base/form.html',context)

def updatetask(request,pk):
    llist=List.objects.get(id=pk)
    form=ListForm(instance=llist)
    if request.method == 'POST':
        form=ListForm(request.POST,instance=llist)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'base/form.html',context)

def deletetask(request,pk):
    llist=List.objects.get(id=pk)
    
    if request.method == 'POST':
        llist.delete()
        return redirect('home')

    context={'obj':llist}
    return render(request,'base/delete.html',context)