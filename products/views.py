from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from mixing_potions_api.permissions import IsOwnerOrReadOnly


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        OrderingFilter,
        SearchFilter
        ]
    ordering_fields = ['name', 'condition__name', 'body_systems__name']
    search_fields = ['name', 'condition__name', 'body_systems__name']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'
