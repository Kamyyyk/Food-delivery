from django.db import models


class Food(models.Model):
    description = models.CharField(max_length=30)
    calories = models.IntegerField()
    created = models.DateTimeField()


class Exercises(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    burned_calories = models.IntegerField




