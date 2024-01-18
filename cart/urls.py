from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:food_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:food_id>/', views.cart_remove, name='cart_remove'),
    path('clear/', views.clear, name='clear'),
    path('order/', views.order, name='order'),
]
