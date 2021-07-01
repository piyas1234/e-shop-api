from api.models import Slider
from api.models import BrandName, Order, Product, TypesofProduct
from rest_framework import serializers
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class TypesofProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesofProduct
        fields = ['name']
    


class BrandNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandName
        fields = ['name']
     

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_Name','product_type','product_brand','product_image1','product_image2','product_image3','product_price','product_description']




class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['title','image']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_user','order_product']
 