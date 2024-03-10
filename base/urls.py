from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('signup/',views.registerPage,name="signup"),
    path('logout/',views.logoutPage,name="logout"),
    path('',views.home,name="home"),
    path('addtask/',views.addtask,name="addtask"),
    path('updatetask/<str:pk>/',views.updatetask,name="updatetask"),
    path('deletetask/<str:pk>/',views.deletetask,name="deletetask"),
]

