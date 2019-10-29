from django.db import models
from datetime import datetime
from django.utils.timezone import now

class StitchType(models.Model):
    name = models.CharField(max_length=50)
    image_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'stitch_type'
        managed = True
        verbose_name = 'Stitch_type'
        verbose_name_plural = 'stitch_types'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.updated_at and self.created_at != self.updated_at:
            self.updated_at = datetime.now()
        super(StitchType, self).save(*args, **kwargs)
 

class StitchTypeDesign(models.Model):
    name = models.CharField(max_length=50)
    image_name = models.CharField(max_length=50)
    stitch = models.ForeignKey(StitchType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'stitch_type_design'
        managed = True
        verbose_name = 'stitch_type_design'
        verbose_name_plural = 'stitch_type_designs'
    
    def __str__(self):
        return self.name
    
    def update(self, *args, **kwargs):
        kwargs.update({'updated_at': now})
        super().update(*args, **kwargs)

        return self