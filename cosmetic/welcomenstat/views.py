import os

from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = ['Главная', 'Адреса', 'Профиль', 'Корзина']


def main_page(request):
    pos = cosmetics.objects.all()
    return render(request, 'welcome_temp/main_stat.html', {'posit': pos, 'menu': menu})


def address(request):
    return render(request, 'welcome_temp/address.html', {'menu': menu})


