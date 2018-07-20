from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='homeview'),
    url(r'^save$', views.SaveData, name='savedata'),
    url(r'^view$', views.ViewEvents, name='viewevent'),
    
]