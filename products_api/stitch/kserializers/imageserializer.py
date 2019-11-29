from rest_framework import serializers
from ..kmodels.imagemodel import KImage


class KImageSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = KImage
        fields = ('id', 'image','description')
        # fields = '__all__'

    def create(self, validated_data):
        mydata = validated_data
        img = KImage.objects.create(**validated_data)
        return img
