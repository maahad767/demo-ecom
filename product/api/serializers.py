from django.core.exceptions import ValidationError
from rest_framework import serializers
from product.models import Category, Product, SellProduct, RentProduct


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        validated_data['owner'] = self.context['request'].user
        product = super().create(validated_data)
        product.categories.add(*categories)
        return product

    class Meta:
        model = Product
        exclude = ['owner', 'is_rented', 'is_sold',
                   'is_for_sell', 'is_for_rent', ]


class SellProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(is_sold=False, is_rented=False))

    def validate(self, attrs):
        buyer = self.context['request'].user
        product = attrs['product']
        if product and buyer == product.owner:
            raise ValidationError(
                {'buyer': 'You can not buy your own products!'})
        attrs['buyer'] = buyer
        return super().validate(attrs)

    class Meta:
        model = SellProduct
        exclude = ['buyer']


class RentProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(is_sold=False, is_rented=False))

    def validate(self, attrs):
        """
        Validates if a user is trying to buy his own products or not!
        """
        borrower = self.context['request'].user
        product = attrs['product']
        if product and borrower == product.owner:
            raise ValidationError(
                {'borrower': 'You can not buy your own products!'})
        attrs['borrower'] = borrower
        return super().validate(attrs)

    class Meta:
        model = RentProduct
        exclude = ['borrower']
