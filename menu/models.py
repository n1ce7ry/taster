from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name



class Food(models.Model):
    name = models.CharField(max_length=60)
    weight = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
