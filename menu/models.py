from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    priority = models.IntegerField()


    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=80)
    weight = models.IntegerField()
    description = models.CharField(max_length=255)
    calories = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='menu/')
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
