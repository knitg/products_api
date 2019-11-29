from django.shortcuts import render 
from .models import KImage, Stitch, StitchType, StitchTypeDesign, Product
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

from .kserializers.imageserializer import KImageSerializer
from .kserializers.stitchserializer import StitchSerializer
from .kserializers.stitchtypeserializer import StitchTypeSerializer, StitchTypeByStitchSerializer
from .kserializers.stitchdesignserializer import StitchTypeDesignSerializer
from .kserializers.productserializer import ProductSerializer

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
    
    def create(self, request, *args, **kwargs):
        if request.FILES:
            request.data['images'] = request.FILES

        stitch_serializer = StitchSerializer(data= request.data)
        if stitch_serializer.is_valid():
            stitch_serializer.save()
            return Response({'stitchId':stitch_serializer.instance.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(stitch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StitchTypeViewSet(viewsets.ModelViewSet):
    queryset = StitchType.objects.all()
    serializer_class = StitchTypeSerializer

    def create(self, request, *args, **kwargs):
        if request.FILES:
            request.data['images'] = request.FILES 

        stitchtype_serializer = StitchTypeSerializer(data= request.data)
        if stitchtype_serializer.is_valid():
            stitchtype_serializer.save()
            return Response({'stitchTypeId':stitchtype_serializer.instance.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(stitchtype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StitchTypeDesignViewSet(viewsets.ModelViewSet):
    queryset = StitchTypeDesign.objects.all()
    serializer_class = StitchTypeDesignSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        if request.FILES:
            request.data['images'] = request.FILES 

        product_serializer = ProductSerializer(data= request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'productId':product_serializer.instance.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def update(self, request, *args, **kwargs):
        if request.FILES:
            request.data['images'] = request.FILES        
        serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
 
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        for e in instance.images.all():
            instance.images.remove(e)
            KImage.objects.get(id=e.id).delete()
        
'''
## PRODUCTS BY USER
'''
class ProductByUserViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        u_id = self.kwargs['user_id']
        return Product.objects.filter(user=u_id)

'''
## STICH TYPE BY STICH CATEGORY
'''
class StitchTypeByStitchViewSet(viewsets.ModelViewSet):
    queryset = StitchType.objects.all()
    serializer_class = StitchTypeByStitchSerializer

    def get_queryset(self):
        stitch = self.kwargs['stitch_id']
        return StitchType.objects.filter(stitch=stitch)























