from gc import get_objects
from msilib.schema import ODBCSourceAttribute
from multiprocessing import get_context
from pprint import pprint
from typing import get_args
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Company, UserServiceVehicle, Vehicle, Type,User
from .pagination import DefaultPagination
from .serializers import CompanySerializer, TypeSerializer, UserSerializer,  UserServiceVehicleSerializer, VehcileSerializer
from .filters import VehicleFilter
from rest_framework.decorators import api_view
from django.db.models.functions import Cast
from django.db.models import TextField

from dealership import serializers

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.prefetch_related('type').all()
    serializer_class = VehcileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = VehicleFilter
    pagination_class = DefaultPagination
    search_fields = ['manufacturer','model']
    ordering_fields = ['price', 'horsepower']

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer



# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

@api_view(['GET','POST'])
def user_list(request):
    if request.method == "GET":
        queryset = User.objects.prefetch_related('vehicle').all()
        serializer = UserSerializer(queryset,many=True)
        
        
        return Response(serializer.data)
    elif request.method == "POST":

        try:
            
            for vehicle_id in request.data['vehicle']:
                vehicle = Vehicle.objects.get(id = vehicle_id)
                company_id = vehicle.company_id
                company = Company.objects.get(id = company_id)
                company.revenue += vehicle.price
                company.save()

                vehicle.quantity -= 1
                vehicle.save()
               
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({'error': 'This vehicle is no longer available we are sorry.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    user = get_object_or_404(User.objects.all(),pk=pk)
    # funkcija za zimanje id na vozilo kaj userot
    old_vehicles = list(User.objects.filter(pk=pk).annotate(str_id=Cast('vehicle', output_field=TextField())).values_list('str_id',flat=True))
    
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":

        for vehicle_id in request.data['vehicle']:
            
            if vehicle_id not in old_vehicles:
                pprint(vehicle_id)
                pprint(old_vehicles)
                vehicle = Vehicle.objects.get(id = vehicle_id)
                vehicle.quantity -= 1
                vehicle.save()
                company_id = vehicle.company_id
                company = Company.objects.get(id = company_id)
                company.revenue += vehicle.price
                company.save()

        serializer = UserSerializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

@api_view(['GET','POST'])
def userservicevehicle_list(request):
    if request.method == "GET":
        queryset = UserServiceVehicle.objects.all()
        serializer = UserServiceVehicleSerializer(queryset,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":

        serializer = UserServiceVehicleSerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT'])
def userservicevehicle_detail(request,pk):
    
    userservicevehicle = get_object_or_404(UserServiceVehicle.objects.all(),pk=pk)
    if request.method == "GET":
        serializer = UserServiceVehicleSerializer(userservicevehicle)
        pprint(userservicevehicle.payment_status)
        return Response(serializer.data)
    
    elif request.method == "PUT":

        serializer = UserServiceVehicleSerializer(userservicevehicle,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if userservicevehicle.payment_status == "C":
            userservicevehicle.service_status = "F"
        elif userservicevehicle.payment_status != "C":
            UserServiceVehicle.objects.filter(service_status)
        return Response(serializer.data,status=status.HTTP_200_OK)

    

class UserServiceVehicleViewSet(ModelViewSet):


    queryset = UserServiceVehicle.objects.all()
    serializer_class = UserServiceVehicleSerializer