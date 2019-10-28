from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now='true')

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name
 



class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'SubCategory'
        managed = True
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategorys'
    
    def __str__(self):
        return self.name