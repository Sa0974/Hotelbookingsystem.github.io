# Generated by Django 4.2.1 on 2023-07-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_userbooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbooking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Available', 'Available'), ('Not Available', 'Not Available')], default='Pending', max_length=20),
        ),
    ]