from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name, self.surname


class Food(models.Model):
    description = models.CharField(max_length=30)
    calories = models.IntegerField(default=0)
    created = models.DateTimeField()

    def __str__(self):
        return self.description


class Exercises(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    burned_calories = models.IntegerField(default=0)
    test = models.CharField(max_length=10)
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
