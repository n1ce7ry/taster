from . import views
from django.urls import path

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<slug:food_type>', views.food_by_type, name='food-by-type'),
]
