from django.shortcuts import get_object_or_404, render
from menu.models import Food, FoodType
from cart.forms import CartAddFoodForm


def menu(request):

    foods = Food.objects.select_related('food_type').order_by(
            'food_type__priority',
            'food_type__name',
            )

    food_dict = {}

    for food in foods:
        food_type = food.food_type
        if food_type not in food_dict:
            food_dict[food_type] = []
        if len(food_dict[food_type]) < 5:
            food_dict[food_type].append(food)

    cart_product_form = CartAddFoodForm()

    
    context = {
        'foods': food_dict,
        'food_types': FoodType.objects.all(),
        'cart_product_form': cart_product_form,
    }

    return render(request, 'menu/menu.html', context=context)


def food_by_type(request, food_type):

    food_type = get_object_or_404(FoodType, slug=food_type)
    foods = Food.objects.filter(food_type__name=food_type)

    context = {
        "foods": foods, 
        "food_type": food_type,
    }
    
    return render(request, 'menu/food_by_type.html', context=context)
