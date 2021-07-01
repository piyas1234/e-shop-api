from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class TypesofProduct(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class BrandName(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    product_Name = models.CharField(max_length=100)
    product_type = models.ForeignKey(
        TypesofProduct,   on_delete=models.CASCADE)
    product_brand = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    product_image1 = models.CharField(max_length=200)
    product_image2 = models.CharField(max_length=200)
    product_image3 = models.CharField(max_length=200)
    product_price = models.CharField(max_length=20)
    product_description = models.CharField(max_length=2000)

    def __str__(self):
        return self.product_Name


class Slider(models.Model):
    title = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_user.username
