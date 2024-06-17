# backend/productos/views.py

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['categoria', 'marca', 'modelo', 'año']  # Asegúrate de que estos campos existen en el modelo
    ordering_fields = ['precio', 'fecha_creacion']
