# Generated by Django 4.2.1 on 2023-07-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(upload_to='uploads/card')),
            ],
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(upload_to='uploads/carousel'),
        ),
    ]
