# Generated by Django 2.2.6 on 2019-11-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stitch', '0002_auto_20191127_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
