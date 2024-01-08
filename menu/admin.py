from django.contrib import admin

from menu.models import Food, FoodType


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    pass
