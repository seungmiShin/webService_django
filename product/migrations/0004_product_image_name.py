# Generated by Django 4.0.5 on 2022-06-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='이미지명'),
        ),
    ]
