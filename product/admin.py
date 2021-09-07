from django.contrib import admin

from .models import Category, Product, SellProduct, RentProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SellProduct)
admin.site.register(RentProduct)
