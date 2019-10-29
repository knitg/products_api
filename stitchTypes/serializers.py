from rest_framework import serializers
from .models import StitchType, StitchTypeDesign

class StitchTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StitchType
        fields = ['id', 'name', 'url', 'created_at', 'updated_at']


class StitchTypeDesignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StitchTypeDesign
        fields = ['id', 'name', 'stitch', 'url', 'created_at', 'updated_at']