from pprint import pprint
from unicodedata import name
from django.contrib import admin

from . import models

@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['type','manufacturer','model','horsepower','cubic_meters','year','price','quantity']
    list_editable = ['price','quantity']
    search_fields = ['manufacturer__istartswith'] 
    lists_per_page = 10
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']
    list_editable = ['email']
    ordering = ['first_name','last_name']
    search_fields = ['first_name__istartswith','last_name__istartswith'] # i is for insenitive case 
    lists_per_page = 10

@admin.register(models.UserServiceVehicle)
class UserServiceVehicle(admin.ModelAdmin):
    list_display = ['user','vehicle','placed_at','payment_status','service_status']
    list_editable = ['payment_status','service_status']
    lists_per_page = 10
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name','CEO']
    list_editable = ['CEO']

admin.site.register(models.Type)


