from re import search
from turtle import update
from rest_framework import serializers
from .models import *

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ['id','type']


class VehcileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Vehicle
        fields = ['id','type','company','manufacturer','model','horsepower','cubic_meters','color','year','price','quantity']

    


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','vehicle']


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id','company_name','CEO','revenue']

    