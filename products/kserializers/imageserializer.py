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

    def update(self, instance, validated_data):
        # Update the Foo instance
        instance.description = validated_data['description']

        
        instance.save()

        if self.initial_data.get('images'):
            validated_data['images'] = self.initial_data['images']
            image_data = validated_data.pop('images')

            ### Remove relational images if any ####
            # for e in instance.images.all():
            #     instance.images.remove(e)
            #     KImage.objects.get(id=e.id).delete()
            # for image in image_data:
            #     c_image= image_data[image]
            #     images = KImage.objects.create(image=c_image, description=self.initial_data.get('description'), source='product_'+str(instance.id), size=c_image.size)
            #     instance.images.add(images)

        return instance
