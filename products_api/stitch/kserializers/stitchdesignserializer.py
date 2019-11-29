from rest_framework import serializers
from products_api.stitch.models import KImage, Stitch, StitchType, StitchTypeDesign, Product
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from .imageserializer import KImageSerializer

class StitchTypeDesignSerializer(serializers.HyperlinkedModelSerializer):
    images = KImageSerializer(many=False, required=False, allow_null=True)
    class Meta:
        model = StitchTypeDesign
        fields = ('sdesign', 'code', 'description', 'stitch_type', 'images')