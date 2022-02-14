from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from dealership.models import Vehicle, Type,User
from dealership.pagination import DefaultPagination
from dealership.serializers import TypeSerializer, UserSerializer, VehcileSerializer
from dealership.filters import VehicleFilter
from rest_framework.decorators import api_view

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
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


