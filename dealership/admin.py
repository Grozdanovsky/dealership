from unicodedata import name
from django.contrib import admin

from . import models

@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['type','manufacturer','model','horsepower','cubic_meters','year','price']
    list_editable = ['price']
    lists_per_page = 10
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    list_editable = ['email']
    ordering = ['first_name','last_name']
    lists_per_page = 10

@admin.register(models.UserServiceVehicle)
class UserServiceVehicle(admin.ModelAdmin):
    list_display = ['user','vehicle','placed_at','payment_status','service_status']
    list_editable = ['payment_status']
    lists_per_page = 10

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name','CEO']
    list_editable = ['CEO']

admin.site.register(models.Type)


