from django.contrib import admin
from .models import BrandName, Order, Product, Slider, TypesofProduct
 
admin.site.register(Product)
admin.site.register(TypesofProduct)
admin.site.register(BrandName)
admin.site.register(Slider)
admin.site.register(Order)