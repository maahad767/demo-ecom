from rest_framework import serializers

from product.models import Category, Product, SellProduct, RentProduct


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class SellProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellProduct
        fields = '__all__'


class RentProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentProduct
        fields = '__all__'
