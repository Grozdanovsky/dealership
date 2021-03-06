from pprint import pprint
from unicodedata import name
from django.contrib import admin
from . import models

class RevenueFilter(admin.SimpleListFilter):
    title = 'Revenue'
    parameter_name = 'Revenue'

    def lookups(self, request, model_admin):
         return [
             ('<500000' ,'Less than $500,000'),
             ('>500000' , 'More than $500,000')
         ]
    
    def queryset(self, request, queryset):
        if self.value() == '<500000':
            return queryset.filter(revenue__lt = 500000)
        if self.value() == '>500000':
            return queryset.filter(revenue__gt = 500000)


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['company']
    list_display = ['type','manufacturer','model','horsepower','cubic_meters','year','price','quantity']
    list_editable = ['price','quantity']
    search_fields = ['manufacturer__istartswith'] 
    list_filter = ['manufacturer']
    lists_per_page = 10
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    autocomplete_fields = ['vehicle']
    list_display = ['first_name','last_name','email']
    list_editable = ['email']
    ordering = ['first_name','last_name']
    search_fields = ['first_name__istartswith','last_name__istartswith'] # i is for insenitive case 
    lists_per_page = 10

@admin.register(models.UserServiceVehicle)
class UserServiceVehicle(admin.ModelAdmin):
    autocomplete_fields = ['user','vehicle']
    list_display = ['user','vehicle','placed_at','payment_status','service_status']
    list_editable = ['payment_status','service_status']
    list_filter = ['payment_status','service_status','placed_at']
    lists_per_page = 10
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    exclude = ['revenue']
    list_display = ['company_name','CEO']
    list_editable = ['CEO']
    list_filter = [RevenueFilter]
    search_fields = ['company_name'] # this is so that i can make autocomplete field in VehicleAdmin class becouse it is a related field.

admin.site.register(models.Type)


