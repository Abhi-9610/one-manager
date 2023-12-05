# Generated by Django 4.1.13 on 2023-11-26 06:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_hoteldetails_remove_customuser_geo_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='hotel_details',
        ),
        migrations.AddField(
            model_name='customuser',
            name='geo_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gst_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='hotel_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_hotel',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='official_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reg_num',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='HotelDetails',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
    ]
