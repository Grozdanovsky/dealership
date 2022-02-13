from django_filters.rest_framework import FilterSet
from .models import Vehicle
class VehicleFilter(FilterSet):
    class Meta:
        model = Vehicle
        fields = {
            'type' : ['exact'],
            'manufacturer' : ['exact'],
            'price' : ['gt' , 'lt'],
            'year' : ['gt' , 'lt'],
            'horsepower' : ['gt' , 'lt'],
        }