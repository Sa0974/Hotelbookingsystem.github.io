# Generated by Django 4.2.1 on 2023-06-20 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_carouselimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(upload_to='carousel/'),
        ),
    ]
