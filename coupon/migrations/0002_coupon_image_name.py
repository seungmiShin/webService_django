# Generated by Django 4.0.5 on 2022-06-16 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='image_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='이미지명'),
        ),
    ]
