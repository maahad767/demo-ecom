# Generated by Django 3.2.7 on 2021-09-07 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Rent')),
                ('is_for_rent', models.BooleanField(default=False, editable=False, verbose_name='For Rent?')),
                ('is_for_sell', models.BooleanField(default=False, editable=False, verbose_name='For Sell?')),
                ('is_sold', models.BooleanField(default=False, verbose_name='Is the product sold?')),
                ('is_rented', models.BooleanField(default=False, verbose_name='Is the product on rent?')),
                ('categories', models.ManyToManyField(to='product.Category', verbose_name='Categories')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Product Owner')),
            ],
        ),
        migrations.CreateModel(
            name='SellProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_at', models.DateTimeField(verbose_name='Selling Time')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Product Buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product Sold')),
            ],
        ),
        migrations.CreateModel(
            name='RentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_starts', models.DateTimeField(verbose_name='Rent Period Starts From')),
                ('rent_ends', models.DateTimeField(verbose_name='Rent Period Ends')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Product Borrower')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product to Rent')),
            ],
        ),
    ]
