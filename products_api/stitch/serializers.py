from rest_framework import serializers
from .models import KImage, Stitch, StitchType, StitchTypeDesign, Product, Vendor

class KImageSerializer(serializers.HyperlinkedModelSerializer): 
    url = serializers.HyperlinkedIdentityField(view_name='upload-detail', source='image',)
    class Meta:
        model = KImage
        fields = ('id', 'image','description', 'url')
        # fields = '__all__'

    def create(self, validated_data):
        mydata = validated_data
        img = KImage.objects.create(**validated_data)
        return img

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class StitchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stitch
        fields = '__all__'
        

class StitchTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StitchType
        fields = '__all__'

class StitchTypeDesignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StitchTypeDesign
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # stitch = StitchSerializer(many=False)
    class Meta:
        model = Product
        fields = '__all__'


























