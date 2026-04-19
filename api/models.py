from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=155)
    color = models.CharField(max_length=155)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.color}"

class Drive(models.Model):
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=155)
    price = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.phone}"

