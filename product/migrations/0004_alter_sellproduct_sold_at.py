# Generated by Django 3.2.7 on 2021-09-07 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210907_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproduct',
            name='sold_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Selling Time'),
            preserve_default=False,
        ),
    ]
