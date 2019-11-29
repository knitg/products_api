from rest_framework import serializers
from products_api.stitch.models import KImage, Stitch, StitchType, StitchTypeDesign, Product
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from .imageserializer import KImageSerializer
from .stitchserializer import StitchSerializer


class StitchTypeSerializer(serializers.HyperlinkedModelSerializer):
    stitch = StitchSerializer(many=False, required=False)
    images = KImageSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = StitchType
        fields = ('stype', 'code', 'description', 'stitch', 'images')

    def create(self, validated_data):
        ## Image data
        if self.initial_data['stitch']:
            stitchQuerySet = Stitch.objects.filter(id= self.initial_data['stitch'])
            stitch = serializers.PrimaryKeyRelatedField(queryset=stitchQuerySet, many=False)
            if len(stitchQuerySet):
                validated_data['stitch'] = stitchQuerySet[0]

        stitchtype = StitchType.objects.create(**validated_data)
        stitchtype.save()

        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')
            for image in image_data:
                c_image= image_data[image]
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='stitchtype_'+str(stitchtype.id), size=c_image.size)
                stitchtype.images.add(images)         

        return stitchtype

class StitchTypeByStitchSerializer(serializers.HyperlinkedModelSerializer):
    # stitch = StitchSerializer(many=False, required=False)
    images = KImageSerializer(many=True, required=False, allow_null=False)
    # stitch = StitchSerializer(many=False)
    class Meta:
        model = StitchType
        fields = ('stype', 'code', 'description', 'images')