from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Producto
from .serializers import ProductoSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.orderingFilter]
    filterset_fields = ['categoria', 'marca', 'modelo' 'año']
    ordering_fields = ['precio', 'fecha_creacion']
    
    