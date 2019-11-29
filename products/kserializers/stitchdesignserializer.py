from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from .imageserializer import KImageSerializer

from ..kmodels.imagemodel import KImage
from ..kmodels.stitchmodel import Stitch
from ..kmodels.stitchtypemodel import StitchType
from ..kmodels.stitchdesignmodel import StitchTypeDesign
from ..kmodels.productmodel import Product

class StitchTypeDesignSerializer(serializers.HyperlinkedModelSerializer):
    images = KImageSerializer(many=False, required=False, allow_null=True)
    class Meta:
        model = StitchTypeDesign
        fields = ('sdesign', 'code', 'description', 'stitch_type', 'images')