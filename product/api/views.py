from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404
from django.db.models import Q

from ..models import Category, Product, SellProduct, RentProduct
from .serializers import CategorySerializer, ProductSerializer, SellProductSerializer, RentProductSerializer
from .filters import BrowseProductFilter


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class SingleProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['pk'], owner=self.request.user)


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['pk'], owner=self.request.user)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['pk'], owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Deleted'}, status=HTTP_204_NO_CONTENT)


class BrowseProductView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrowseProductFilter

    def get_queryset(self):
        return Product.objects.filter(is_sold=False, is_rented=False).filter(~Q(owner=self.request.user))


class ProductSellView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SellProductSerializer


class ProductRentView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RentProductSerializer


class ProductSoldListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_sold=True, is_rented=False).filter(owner=self.request.user)


class ProductLentListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_sold=False, is_rented=True).filter(owner=self.request.user)


class ProductBoughtListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_sold=True, is_rented=False).filter(sold__buyer=self.request.user)


class ProductBorrowedListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_sold=True, is_rented=False).filter(lent__borrower=self.request.user)
