from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('signup/',views.registerPage,name="signup"),
    path('logout/',views.logoutPage,name="logout"), 
    path('addtask/',views.addtask,name="addtask"),
    path('deletetask/<str:pk>/',views.deletetask,name="deletetask"),
    path('',views.home,name="home"),
]

