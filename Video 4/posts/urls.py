from django.contrib import admin
from django.urls import path
from posts import views as views

urlpatterns = [
   path('',views.home, name='home'),
   path('blogposts',views.blogposts, name='blogposts')
]
