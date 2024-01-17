import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import Food
from .cart import Cart
from django.contrib.sessions.exceptions import SessionInterrupted


@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)


    try:
        data = json.loads(request.body)
        quantity = data.get('quantity')
        update = data.get('update')
        cart.add(food=food,
                quantity = quantity,
                update_quantity = update,)
        return JsonResponse({'success': 'success', 'total_cart_price': cart.get_total_price(),
                             'total_quantity': cart.get_total_quanity(), 'food': food.name })


    except Exception:
        raise SessionInterrupted


def cart_remove(request, food_id):
    cart = Cart(request)
    product = get_object_or_404(Food, id=food_id)
    cart.remove(product)

    return redirect('cart_detail')


def clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
