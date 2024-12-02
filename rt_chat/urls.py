from django.urls import path 
from .views import *
from django.contrib import admin
from rt_chat import views

urlpatterns = [
    path('',chat_view,name="chat"),
    path('profile',views.profile,name="profile"),
    path('chat/<username>',get_or_create_chatroom,name="start-chat"),
    path('chat/room/<chatroom_name>',chat_view,name="chatroom"),
    path('public_chatrooms/', views.public_chatrooms_list, name="public_chatrooms_list"),
]
