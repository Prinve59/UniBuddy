from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('register',views.register,name="register"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
]
