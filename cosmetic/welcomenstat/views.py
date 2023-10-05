from django.http import HttpResponse
from django.shortcuts import render

import cosmetic

# Create your views here.
menu = ['Рожки','Ножки','Ложки','Кошки']

def main_page(request):
    return render(request, 'welcome_temp/main_stat.html', {'menu': menu})
