from typing import List
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from product.models import Category, Product, SellProduct, RentProduct
from .serializers import CategorySerializer, ProductSerializer, SellProductSerializer, RentProductSerializer


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = IsAuthenticated


class SingleProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = IsAuthenticated


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = IsAuthenticated


# TODO Product Filter View: Filter Based on Title, Price Range, Categories, Buy/Rent type

# TODO Product Sell View, Product Rent View
