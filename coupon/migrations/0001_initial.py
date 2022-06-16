# Generated by Django 4.0.5 on 2022-06-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='제품명')),
                ('price', models.IntegerField()),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='카테고리')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]