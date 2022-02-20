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

    def __str__(self) -> str:
        return self.company_name

    class Meta:

        ordering = ['id']


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    horsepower = models.PositiveIntegerField()
    cubic_meters = models.PositiveIntegerField()
    color = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    service_cost = models.PositiveIntegerField()


    def __str__(self) -> str:
        return f'{self.manufacturer} {self.model}'
    class Meta:
        
        ordering = ['company']
    
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    vehicle = models.ManyToManyField(Vehicle, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name}  {self.last_name}'




class UserServiceVehicle(models.Model):

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    
    ]

    SERVICE_STATUS_FINISHED = 'F'
    SERVICE_STATUS_UNFINISHED = 'X'

    SERVICE_STATUS_CHOICES = [
        
        (SERVICE_STATUS_FINISHED, 'Finished'),
        (SERVICE_STATUS_UNFINISHED, 'Unfinished')

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    service_status = models.CharField(max_length=1, choices=SERVICE_STATUS_CHOICES, default = SERVICE_STATUS_UNFINISHED)

