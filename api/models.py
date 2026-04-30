from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    name = models.CharField(max_length=155)
    color = models.CharField(max_length=155)
    year = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cars')

    def __str__(self):
        return f"{self.name} {self.color}"

class Drive(models.Model):
    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=155)
    price = models.IntegerField()
    age = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='drives')

    def __str__(self):
        return f"{self.name} {self.phone}"

