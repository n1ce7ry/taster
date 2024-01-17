from decimal import Decimal
from django.conf import settings
from menu.models import Food


class Cart(object):

    def __init__(self, request):
        """
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())


    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        food_ids = self.cart.keys()
        foods = Food.objects.filter(id__in=food_ids)
        for food in foods:
            self.cart[str(food.id)]['food'] = food

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def add(self, food, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity': 0,
                                     'price': str(food.price)}
        if update_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, food):
        """
        Удаление товара из корзины.
        """
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()


    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())


    def get_total_quanity(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        """ удаление корзины из сессии """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
