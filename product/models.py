from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rest_framework.fields import ChoiceField


class Category(models.Model):
    """Database model for Product Category, can't have sub-category"""
    name = models.CharField(_("Category Name"), max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for Product
    A product can have both price and rent. Price not null/None means, the product is for Sell and 
    Rent null/None 0 means, the product is for Rent. A product can be in both list together, 
    Once the product is sold, It can not be sold or rented anymore.
    """
    owner = models.ForeignKey(get_user_model(), verbose_name=_(
        "Product Owner"), on_delete=models.CASCADE, related_name="products")
    name = models.CharField(_("Product Name"), max_length=50)
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    description = models.TextField(_("Description"))
    price = models.DecimalField(
        _("Price"), max_digits=10, decimal_places=2, null=True)
    rent = models.DecimalField(
        _("Rent"), max_digits=10, decimal_places=2, null=True)
    rent_type = ChoiceField(choices=[(
        'hourly', 'hourly'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ])
    is_sold = models.BooleanField(
        _("Is the product sold?"), default=False)
    is_rented = models.BooleanField(
        _("Is the product on rent?"), default=False)

    def __str__(self):
        return self.name


class SellProduct(models.Model):
    """Database model for storing selling information, implemented simply."""
    product = models.ForeignKey(Product, verbose_name=_(
        "Product Sold"), on_delete=models.CASCADE)
    buyer = models.ForeignKey(get_user_model(), verbose_name=_(
        "Product Buyer"), on_delete=models.CASCADE)
    sold_at = models.DateTimeField(_("Selling Time"), auto_now_add=False)

    def __str__(self):
        return self.product.name


class RentProduct(models.Model):
    """Database model for tracking Product Rent's data"""
    product = models.ForeignKey(Product, verbose_name=_(
        "Product to Rent"), on_delete=models.CASCADE)
    borrower = models.ForeignKey(get_user_model(), verbose_name=_(
        "Product Borrower"), on_delete=models.CASCADE)
    rent_starts = models.DateTimeField(
        _("Rent Period Starts From"))
    rent_ends = models.DateTimeField(
        _("Rent Period Ends"))

    def __str__(self):
        return self.product.name
