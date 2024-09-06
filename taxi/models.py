from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} {self.country}"

class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver")

class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True, blank=True, null=True)

