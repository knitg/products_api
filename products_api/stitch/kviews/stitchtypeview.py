from django.shortcuts import render 
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from ..kmodels.stitchtypemodel import StitchType
from ..kserializers.stitchtypeserializer import StitchTypeSerializer, StitchTypeByStitchSerializer


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

'''
        STICH TYPE BY STICH CATEGORY
'''
class StitchTypeByStitchViewSet(viewsets.ModelViewSet):
    queryset = StitchType.objects.all()
    serializer_class = StitchTypeByStitchSerializer

    def get_queryset(self):
        stitch = self.kwargs['stitch_id']
        return StitchType.objects.filter(stitch=stitch)