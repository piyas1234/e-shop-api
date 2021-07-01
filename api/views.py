from api.models import Slider
from api.models import BrandName, Product, TypesofProduct
from .serializers import BrandNameSerializer, ProductSerializer, SliderSerializer, TypesofProductSerializer, UsersSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


 

class typeProduct_ListView(APIView):
    def get_object(self, type):
        try:
            return Product.objects.get(product_type=type)
        except ProductSerializer.DoesNotExist:
            raise Http404

    def get(self, request, type, format=None):
        snippet = self.get_object(type)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

 

class Brand_ListView(APIView):
    def get_object(self, type):
        try:
            return Product.objects.get(product_brand=type)
        except ProductSerializer.DoesNotExist:
            raise Http404

    def get(self, request, type, format=None):
        snippet = self.get_object(type)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

 


 
 
class Product_ListView(APIView):
   
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleProduct_ListView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except ProductSerializer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 

class TypesofAllProductView(APIView):
   
    def get(self, request, format=None):
        snippets = TypesofProduct.objects.all()
        serializer = TypesofProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypesofProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypesofProductView(APIView):
    def get_object(self, pk):
        try:
            return TypesofProduct.objects.get(pk=pk)
        except TypesofProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TypesofProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TypesofProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 


class BrandNameView(APIView):
   
    def get(self, request, format=None):
        snippets = BrandName.objects.all()
        serializer = BrandNameSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BrandNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllBrandNameView(APIView):
    def get_object(self, pk):
        try:
            return BrandName.objects.get(pk=pk)
        except BrandName.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BrandNameSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BrandNameSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 


class SliderView(APIView):
   
    def get(self, request, format=None):
        snippets = Slider.objects.all()
        serializer = SliderSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllSliderView(APIView):
    def get_object(self, pk):
        try:
            return Slider.objects.get(pk=pk)
        except Slider.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SliderSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SliderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
