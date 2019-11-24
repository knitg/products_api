from django.db import models

from datetime import datetime
from django.utils.timezone import now


from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.
def uploadFolder(instance, filename):
    imgpath= '/'.join(['images', str(instance.source), filename])
    return imgpath

class KImage(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=uploadFolder, max_length=254, blank=True, null=True)
    source = models.CharField(blank=True, null=True, default='', max_length=50)
    size = models.IntegerField(blank=True, null=True, default=0)
    class Meta:
        db_table = 'knit_image'
        managed = True

    def save(self, **kwargs):
        if self.image:
            #Opening the uploaded image
            im = Image.open(self.image)
            output = BytesIO()
            # #Resize/modify the image
            im = im.resize((800, 600), Image.ANTIALIAS)
            # #after modifications, save it to the output
            im.save(output, format='PNG', quality=100)
            
            #change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.png" %self.image.name.split('.')[0], 'image/png', sys.getsizeof(output), None)

        super(KImage, self).save()

    def __str__(self):
        return self.image


class Stitch(models.Model):
    stype= models.CharField(null=True, max_length=80,  default=None)    
    code = models.CharField(null=True, max_length=80,  default=None)
    images = models.ManyToManyField(KImage, blank=True, null=True, default=None)
    description = models.CharField(null=True, max_length=80,  default=None) 
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'knit_stitch'
        managed = True
        verbose_name = 'Knit Stitch Ref Table'
        verbose_name_plural = 'Knit Stitch Ref Table'
    
    def __str__(self):
        return self.stype



class StitchType(models.Model):
    stype= models.CharField(null=True, max_length=80,  default=None) 
    stitch = models.ForeignKey(Stitch, on_delete=models.CASCADE, default=None, null=False) 
    images = models.ManyToManyField(KImage, blank=True, null=True, default=None)
    code = models.CharField(null=True, max_length=80,  default=None) 
    description = models.CharField(null=True, max_length=120,  default=None) 
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'knit_stitch_type'
        managed = True
        verbose_name = 'Knit Stitch Type Ref Table'
        verbose_name_plural = 'Knit Stitch Type Ref Table'
    
    def __str__(self):
        return self.stype



class StitchTypeDesign(models.Model):
    sdesign= models.CharField(null=True, max_length=80,  default=None) 
    stitch_type = models.ForeignKey(StitchType, on_delete=models.CASCADE, default=None, null=False)
    images = models.ManyToManyField(KImage, blank=True, null=True, default=None)
    code = models.CharField(null=True, max_length=80,  default=None) 
    description = models.CharField(null=True, max_length=120,  default=None) 
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'knit_stitch_type_design'
        managed = True
        verbose_name = 'Knit Stitch Type design'
        verbose_name_plural = 'Knit Stitch Type design'
    
    def __str__(self):
        return self.sdesign


class Product(models.Model):
    code = models.CharField(null=True, max_length=80,  default=None) 
    title= models.CharField(null=True, max_length=80,  default=None) 
    description = models.CharField(null=True, max_length=120,  default=None) 
    images = models.ManyToManyField(KImage, blank=True, null=True, default=None)
    stitch = models.ForeignKey(Stitch, on_delete=models.CASCADE, default=None, null=True, blank=True)   
    stitch_type = models.ForeignKey(StitchType, on_delete=models.CASCADE, default=None, null=True, blank=True)   
    stitch_type_design = models.ForeignKey(StitchTypeDesign, on_delete=models.CASCADE, default=None, null=True, blank=True)
    vendor =  models.ForeignKey('self', null=True, related_name="product", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'knit_product'
        managed = True
        verbose_name = 'Knit Product'
        verbose_name_plural = 'Knit Products'
    
    def __str__(self):
        return self.code

