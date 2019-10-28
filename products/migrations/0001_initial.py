# Generated by Django 2.2.6 on 2019-10-28 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategorys',
                'db_table': 'SubCategory',
                'managed': True,
            },
        ),
    ]
