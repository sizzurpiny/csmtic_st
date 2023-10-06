
from django.contrib import admin
from django.urls import path

from welcomenstat import views

urlpatterns = [
    path('', views.main_page),
    path('address/', views.address),
]
