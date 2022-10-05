from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cars
from .serializers import CarsSerializer


# в данном классе делается все то же самое, что в и следующей части кода ниже
class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
# классы представлений. Гогвориться о том, что В первом классе идут запросы get and post
#                                              во втором классе идут запросы put and path
#                                              в третьем классе идут get, put, path, delete

# class CarsAPIList(generics.ListCreateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#
# class CarsAPIUpdate(generics.UpdateAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#
# class CarsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer




