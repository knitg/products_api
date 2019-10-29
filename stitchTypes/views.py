from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StitchTypeSerializer, StitchTypeDesignSerializer
from .models import StitchType, StitchTypeDesign

# Create your views here.
class StitchTypeViewSet(viewsets.ModelViewSet):
    queryset = StitchType.objects.all()
    serializer_class = StitchTypeSerializer

class StitchTypeDesignViewSet(viewsets.ModelViewSet):
    queryset = StitchTypeDesign.objects.all()
    serializer_class = StitchTypeDesignSerializer