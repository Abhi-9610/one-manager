# Generated by Django 4.1.13 on 2023-12-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_delete_room_delete_roomtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='hotel_logo',
            field=models.ImageField(blank=True, default=1, upload_to='hotel_logos/'),
            preserve_default=False,
        ),
    ]
