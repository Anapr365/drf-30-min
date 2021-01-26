from django.shortcuts import render
from rest_framework import viewsets
from .models import cliente
from .serializers import clienteSerializer

# Create your views here.
class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer