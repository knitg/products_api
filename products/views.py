from django.shortcuts import render
from .models import Category, SubCategory
from rest_framework import viewsets
from products.serializers import CategorySerializer, SubCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer