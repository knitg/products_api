# Generated by Django 2.2.6 on 2019-11-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stitch', '0004_auto_20191124_1029'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='stitch.KImage'),
        ),
        migrations.RemoveField(
            model_name='stitch',
            name='images',
        ),
        migrations.AddField(
            model_name='stitch',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='stitch.KImage'),
        ),
        migrations.RemoveField(
            model_name='stitchtype',
            name='images',
        ),
        migrations.AddField(
            model_name='stitchtype',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='stitch.KImage'),
        ),
        migrations.RemoveField(
            model_name='stitchtypedesign',
            name='images',
        ),
        migrations.AddField(
            model_name='stitchtypedesign',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='stitch.KImage'),
        ),
    ]
