# Generated by Django 2.2.6 on 2019-11-22 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stitch', '0002_auto_20191123_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='stitch.Product'),
        ),
    ]