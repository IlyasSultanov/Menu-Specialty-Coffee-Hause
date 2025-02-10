from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('drinks/', views.drinks_menu, name='drinks_menu'),
    path('dishes/', views.dishes_menu, name='dishes_menu'),
    path('desserts/', views.desserts_menu, name='desserts_menu'),
]