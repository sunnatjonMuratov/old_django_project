# Generated by Django 5.0.6 on 2024-06-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
