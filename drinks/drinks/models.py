from django.db import models

class Drink(models.Model):
        name = models.CharField(max_length=150)
        description = models.CharField(max_length=400)


def __str__(self):
           return self.name + '' + self.description