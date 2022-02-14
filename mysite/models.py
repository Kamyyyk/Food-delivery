from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=50)
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Votes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    vote = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


