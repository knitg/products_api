from rest_framework import serializers
from .models import KImage, Stitch, StitchType, StitchTypeDesign, Product
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser

class KImageSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = KImage
        fields = ('id', 'image','description')
        # fields = '__all__'

    def create(self, validated_data):
        mydata = validated_data
        img = KImage.objects.create(**validated_data)
        return img

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
            
class StitchTypeDesignSerializer(serializers.HyperlinkedModelSerializer):
    images = KImageSerializer(many=False, required=False, allow_null=True)
    class Meta:
        model = StitchTypeDesign
        fields = ('sdesign', 'code', 'description', 'stitch_type', 'images')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    stitch = StitchSerializer(many=False, required=False)
    stitch_type = StitchTypeSerializer(many=False, required=False)
    images = KImageSerializer(many=True, required=False, allow_null=False)
    # stitch = StitchSerializer(many=False)
    class Meta:
        model = Product
        fields = ('code', 'title','description', 'stitch','stitch_type','stitch_type_design','user', 'images')
    
    def create(self, validated_data):
        ## Image data
        if self.initial_data['stitch']:
            if self.initial_data['stitch']:
                stitchQuerySet = Stitch.objects.filter(id= self.initial_data['stitch'])
                stitch = serializers.PrimaryKeyRelatedField(queryset=stitchQuerySet, many=False)
            if self.initial_data['stitch_type']:
                stitchTypeQuerySet = StitchType.objects.filter(id= self.initial_data['stitch_type'])
                stitch_type = serializers.PrimaryKeyRelatedField(queryset=stitchTypeQuerySet, many=False)
            if len(stitchQuerySet):
                validated_data['stitch'] = stitchQuerySet[0]
            if len(stitchTypeQuerySet):
                validated_data['stitch_type'] = stitchTypeQuerySet[0]

        product = Product.objects.create(**validated_data)
        product.save()

        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')
            for image in image_data:
                c_image= image_data[image]
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='product_'+str(product.id), size=c_image.size)
                product.images.add(images)         

        return product
        
    def update(self, instance, validated_data):
        # Update the Foo instance
        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.code = validated_data['code']

        if self.initial_data['stitch']:
            stitchQuerySet = Stitch.objects.filter(id= self.initial_data['stitch'])
            # stitch = serializers.PrimaryKeyRelatedField(queryset=stitchQuerySet, many=False)
            instance.stitch = Stitch.objects.filter(id= self.initial_data['stitch'])[0]
        if self.initial_data['stitch_type']:
            # stitchTypeQuerySet = StitchType.objects.filter(id= self.initial_data['stitch_type'])
            # stitch_type = serializers.PrimaryKeyRelatedField(queryset=stitchTypeQuerySet, many=False)
            instance.stitch_type = StitchType.objects.filter(id= self.initial_data['stitch_type'])[0]

        instance.save()
            
        for e in instance.images.all():
            instance.images.remove(e)
            KImage.objects.get(id=e.id).delete()


        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')
            
            for image in image_data:
                c_image= image_data[image]
                images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='product_'+str(instance.id), size=c_image.size)
                instance.images.add(images)

        return instance

class StitchTypeByStitchSerializer(serializers.HyperlinkedModelSerializer):
    # stitch = StitchSerializer(many=False, required=False)
    images = KImageSerializer(many=True, required=False, allow_null=False)
    # stitch = StitchSerializer(many=False)
    class Meta:
        model = StitchType
        fields = ('stype', 'code', 'description', 'images')