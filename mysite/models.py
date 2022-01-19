from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=50)
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Votes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)
    vote = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Food(models.Model):
#     name = models.CharField(max_length=30)
#     description = models.CharField(max_length=30)
#     calories = models.IntegerField(default=0)
#     created = models.DateTimeField()
#
#     def __str__(self):
#         return self.description


