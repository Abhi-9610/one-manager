from rest_framework import serializers
from .models import *

class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = Roomdata
        fields = ["room_types", "room_number"]

class UserSerializer(serializers.ModelSerializer):
    total_rooms = Roomserializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'name', 'hotel_name', 'reg_num', 'gst_number', 'official_email', 'geo_location', 'id_hotel', 'hotel_logo', 'services', 'total_rooms']

    def create(self, validated_data):
        hotel_logo = validated_data.pop('hotel_logo', None)
        total_rooms_data = validated_data.pop('total_rooms', None)

        user = CustomUser.objects.create_user(
            username=validated_data['phone_number'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            name=validated_data['name'],
        )

        if total_rooms_data:
            # Create Roomdata instances and associate them with the user
            for room_data in total_rooms_data:
                Roomdata.objects.create(total_rooms=user, **room_data)

        user.save()

        if hotel_logo:
            user.hotel_logo = hotel_logo
            user.save()

        return user
