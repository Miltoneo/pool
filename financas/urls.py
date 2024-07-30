from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name='financas'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='index'),

]
 