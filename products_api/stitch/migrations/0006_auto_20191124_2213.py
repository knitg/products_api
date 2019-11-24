# Generated by Django 2.2.6 on 2019-11-24 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stitch', '0005_auto_20191124_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stitch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stitch.Stitch'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stitch_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stitch.StitchType'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stitch_type_design',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stitch.StitchTypeDesign'),
        ),
        migrations.AlterField(
            model_name='stitchtype',
            name='stitch',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stitch.Stitch'),
        ),
        migrations.AlterField(
            model_name='stitchtypedesign',
            name='stitch_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stitch.StitchType'),
        ),
    ]
