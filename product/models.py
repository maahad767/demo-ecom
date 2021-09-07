from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rest_framework.fields import CharField, ChoiceField


class Category(models.Model):
    """Database model for Product Category, can't have sub-category"""
    name = models.CharField(_("Category Name"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


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
        _("Price"), max_digits=10, decimal_places=2, null=True, blank=True)
    rent = models.DecimalField(
        _("Rent"), max_digits=10, decimal_places=2, null=True, blank=True)
    is_for_rent = models.BooleanField(
        _("For Rent?"), default=False, editable=False)
    is_for_sell = models.BooleanField(
        _("For Sell?"), default=False, editable=False)

    rent_type = models.CharField(choices=[('not_applicable', 'not_applicable'), (
        'hourly', 'hourly'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ], max_length=50, null=True, blank=True)
    is_sold = models.BooleanField(
        _("Is the product sold?"), default=False)
    is_rented = models.BooleanField(
        _("Is the product on rent?"), default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SellProduct(models.Model):
    """Database model for storing selling information, implemented simply."""
    product = models.ForeignKey(Product, verbose_name=_(
        "Product Sold"), on_delete=models.CASCADE, related_name='sold')
    buyer = models.ForeignKey(get_user_model(), verbose_name=_(
        "Product Buyer"), on_delete=models.CASCADE, related_name='bought')
    sold_at = models.DateTimeField(
        _("Selling Time"), auto_now_add=True)

    def __str__(self):
        return self.product.name


class RentProduct(models.Model):
    """Database model for tracking Product Rent's data"""
    product = models.ForeignKey(Product, verbose_name=_(
        "Product to Rent"), on_delete=models.CASCADE, related_name='lent')
    borrower = models.ForeignKey(get_user_model(), verbose_name=_(
        "Product Borrower"), on_delete=models.CASCADE, related_name='borrowed')
    rent_starts = models.DateTimeField(
        _("Rent Period Starts From"))
    rent_ends = models.DateTimeField(
        _("Rent Period Ends"))

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=Product)
def update_product_listing_type(instance, created, *args, **kwargs):
    """If a product instance is created, based on it's price and rent value
    set if it is for rent, sell or not.

    Args:
        instance (Product): [A product instance, when a product object is created we work on it]
        created : [determine if it is created or is it edited?]
    """

    if not created:
        return

    if instance.price:
        instance.is_for_sell = True
    if instance.rent:
        instance.is_for_rent = True
    else:
        instance.rent_type = 'not_applicable'
    instance.save()


@receiver(post_save, sender=SellProduct)
def update_product_sold(instance, created, *args, **kwargs):
    """If a product is sold, a SellProduct will be created and it will send signal here
    and the product will be updated as sold here

    Args:
        instance (SellProduct): [SellProduct instance]
        created : If not created, it's not a sell, so don't update.
    """
    if not created:
        return

    instance.product.is_sold = True
    instance.product.save()


@receiver(post_save, sender=RentProduct)
def update_product_rent(instance, created, *args, **kwargs):
    """If a product is rented, a RentProduct object will be created and it will send signal here
    and the product will be updated as rented here

    Args:
        instance (RentProduct): [RentProduct instance]
        created : If not created, it's not a new rent, so it won't update product.
    """
    if not created:
        return

    instance.product.is_rented = True
    instance.product.save()
