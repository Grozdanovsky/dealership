from django.db import models
from uuid import uuid4
# Create your models here.

class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.type

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    CEO = models.CharField(max_length=255)
    revenue = models.IntegerField(default=0)
class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    horsepower = models.IntegerField()
    cubic_meters = models.IntegerField()
    color = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()

    
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    vehicle = models.ManyToManyField(Vehicle, blank=True)



