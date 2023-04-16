from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import DogSerializer
from .models import Dog

class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = DogSerializer # tell django what serializer to use

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all().order_by('id')
    serializer_class = DogSerializer