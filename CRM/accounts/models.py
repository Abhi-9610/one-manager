from djongo import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid



class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    # is_signed_out = models.BooleanField(default=False)
    
    # Hotel-Details
    id_hotel = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)
    hotel_name = models.CharField(max_length=25, null=True, blank=True)
    reg_num = models.CharField(max_length=20, null=True, blank=True)
    gst_number = models.CharField(max_length=15, null=True, blank=True)
    official_email = models.EmailField(null=True, blank=True)
    hotel_logo = models.ImageField(upload_to='hotel_logos/', blank=True)
    geo_location = models.CharField(max_length=255, null=True, blank=True)


    SERVICES=[
        ("RES","Resturant"),
        ("SP","Swimming-Pool"),
        ("Bar","Bar"),
        ("Laundary","Laundary"),
        ("Parking","Parking"),
        
    ]
    services=models.CharField(max_length=10,choices=SERVICES,null=True, blank=True)
    
    total_rooms = models.IntegerField(default=None, blank=True, null=True)


   


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

   
class TokenBlacklist(models.Model):
    token = models.CharField(max_length=255, unique=True)


class Roomdata(models.Model):
    room_types = models.CharField(max_length=20)
    total_rooms = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="rooms")
    room_number = models.CharField(max_length=1000, blank=True, default=None)

    def __str__(self):
        return self.room_types
