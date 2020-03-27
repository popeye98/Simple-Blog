from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.AllAuthor,name='authorHhome'),
    path('<str:slug>',views.AboutAuthor,name='AboutAuthor'),
]
