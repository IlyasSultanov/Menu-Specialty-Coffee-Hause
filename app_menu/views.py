from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app_menu/home.html')


def drinks_menu(request):
    return render(request, 'app_menu/drinks.html')


def dishes_menu(request):
    return render(request, 'app_menu/dishes.html')


def desserts_menu(request):
    return render(request, 'app_menu/desserts.html')


