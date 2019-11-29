from rest_framework import serializers
from products_api.stitch.models import KImage, Stitch, StitchType, StitchTypeDesign, Product
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from .imageserializer import KImageSerializer


class StitchSerializer(serializers.HyperlinkedModelSerializer):
    images = KImageSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = Stitch
        fields = ('stype', 'code', 'description', 'images')
        parser_classes = (FormParser, MultiPartParser, FileUploadParser) # set parsers if not set in settings. Edited

    def create(self, validated_data):
        ## Image data 
        stitch = Stitch.objects.create(**validated_data)
        stitch.save()

        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')
            for image in image_data:
                c_image= image_data[image]
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='stitch_'+str(stitch.id), size=c_image.size)
                stitch.images.add(images)         

        return stitch
            