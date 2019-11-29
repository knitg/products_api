from django.shortcuts import render 
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from ..kmodels.stitchdesignmodel import StitchTypeDesign
from ..kserializers.stitchdesignserializer import StitchTypeDesignSerializer

class StitchTypeDesignViewSet(viewsets.ModelViewSet):
    queryset = StitchTypeDesign.objects.all()
    serializer_class = StitchTypeDesignSerializer