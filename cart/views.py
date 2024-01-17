import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import Food
from .cart import Cart
from .forms import CartAddFoodForm


@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddFoodForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        data = json.loads(request.body)
        quantity = data.get('quantity')
        update = data.get('update')
        cart.add(food=food,
                quantity = quantity,
                update_quantity = update,)
        return JsonResponse({'success': 'success', 'total_cart_price': cart.get_total_price(),
                             'total_quantity': cart.get_total_quanity()})

    return redirect('menu')


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
