# forms.py

from django import forms

class HotelDetailsForm(forms.Form):
    hotel_name = forms.CharField(max_length=100)
    reg_num = forms.CharField(max_length=20)
    gst_number = forms.CharField(max_length=20)
    official_email = forms.EmailField()
    geo_location = forms.CharField(max_length=100)
    # hotel_logo=forms.ImageField()

class HotelSetupForm(forms.Form):
    room_types = forms.CharField()
    rooms_per_type = forms.CharField()
    services = forms.CharField()