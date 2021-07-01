# Generated by Django 3.2.4 on 2021-07-01 17:18

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
            name='BrandName',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypesofProduct',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Name', models.CharField(max_length=100)),
                ('product_image1', models.CharField(max_length=200)),
                ('product_image2', models.CharField(max_length=200)),
                ('product_image3', models.CharField(max_length=200)),
                ('product_price', models.CharField(max_length=20)),
                ('product_description', models.CharField(max_length=2000)),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.brandname')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typesofproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
