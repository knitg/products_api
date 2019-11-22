from django.shortcuts import render
from .serializers import KImageSerializer, StitchTypeSerializer, StitchTypeDesignSerializer, StitchSerializer, ProductSerializer, VendorSerializer
from .models import KImage, Stitch, StitchType, StitchTypeDesign, Product, Vendor
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

from rest_framework import viewsets, generics
from rest_framework.response import Response

from rest_framework import status


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    # parser_class = (FileUploadParser,)
    queryset = KImage.objects.all()
    serializer_class = KImageSerializer
    parser_classes = (FormParser, MultiPartParser, FileUploadParser) # set parsers if not set in settings. Edited

    
    def create(self, request, *args, **kwargs):
        images_arr = []
        for image in request.FILES:
            image_serializer = KImageSerializer(data= {'description': request.data['description'], 'image': request.FILES[image]})
            if image_serializer.is_valid():
                image_serializer.save()
                images_arr.append(image_serializer.instance.id)
                return Response({'image_ids': images_arr}, status=status.HTTP_201_CREATED)
            else:
                return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StitchViewSet(viewsets.ModelViewSet):
    queryset = Stitch.objects.all()
    serializer_class = StitchSerializer

class StitchTypeViewSet(viewsets.ModelViewSet):
    queryset = StitchType.objects.all()
    serializer_class = StitchTypeSerializer

class StitchTypeDesignViewSet(viewsets.ModelViewSet):
    queryset = StitchTypeDesign.objects.all()
    serializer_class = StitchTypeDesignSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

























