from django.shortcuts import render 
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from ..kmodels.stitchmodel import Stitch
from ..kserializers.stitchserializer import StitchSerializer


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
