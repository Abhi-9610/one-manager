from django.contrib import admin

from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     # Assuming 'id_hotel' is a field in the 'HotelDetails' model
#     list_display = UserAdmin.list_display 

admin.site.register(CustomUser)


