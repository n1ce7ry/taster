from django.shortcuts import render
from menu.models import Food, FoodType


def menu(request):
    context = {
        'foods': Food.objects.all(),
        'food_types': FoodType.objects.all()
    }
    return render(request, 'menu/menu.html', context=context)