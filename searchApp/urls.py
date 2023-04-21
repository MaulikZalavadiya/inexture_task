from django.contrib import admin
from django.urls import path, include
from searchApp import views

urlpatterns = [
     path('search/<keyword>', views.Amazondata, name='amazondata'),
]