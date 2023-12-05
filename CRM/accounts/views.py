import genericpath
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token




@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.otp = '1234'  # Set the predefined OTP value
        user.save()
        return Response({'detail': 'Account created successfully. OTP sent.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signin_api(request):
    phone_number = request.data.get('phone_number', '')
    otp_entered = request.data.get('otp', '')

    try:
        user = CustomUser.objects.get(username=phone_number)
    except ObjectDoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if user and user.otp == otp_entered:
        user.otp = ''
        user.save()
        
        token, created = Token.objects.get_or_create(user=user)

        if not created:
            return Response({'detail': 'User already logged in.'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.hotel_name:
            response_data={
                'status': 'You have successfully logged in!',
                'has_hotel_details': False,
                'detail': 'Please enter your hotel details.',
                'token': str(token),
                'user': UserSerializer(user).data
            }

            return JsonResponse(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'status': 'Welcome back!',
                'token': str(token),
                'user': UserSerializer(user).data
            }
            response = JsonResponse(response_data, status=status.HTTP_200_OK)
            response['Authorization'] = f'Bearer {token}'
            return response
    else:
        new_otp = generate_new_otp()
        user.otp = new_otp
        user.save()
        return Response({'detail': 'Invalid OTP. New OTP sent.'}, status=status.HTTP_401_UNAUTHORIZED)

def generate_new_otp():
    
    new_otp = '4567'  # Replace with your actual OTP generation logic
    return new_otp




# views.py


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def enter_hotel_details(request):
    user = request.user

    if request.method == 'POST':
   
        # Update the user object with the entered details
        user.hotel_name = request.data.get('hotel_name','')
        user.reg_num = request.data.get('reg_num','')
        user.gst_number = request.data.get('gst_number','')
        user.official_email = request.data.get('official_email','')
        user.geo_location = request.data.get('geo_location','')
        user.total_rooms = request.data.get('total_rooms')
        user.hotel_logo= request.data.get('hotel_logo')
        user.save()

        if not user.hotel_name:
            return Response({
                'message': 'Please enter your hotel details',
                'details': UserSerializer(user).data
             }, status=status.HTTP_400_BAD_REQUEST)
            

        return Response({
            'message': 'Hotel details successfully entered',
            "details":UserSerializer(user).data
            # 'details': UserSerializer(user).data
        }, status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def staff_management(request):
    user = request.user

    if request.method == 'POST':
        # Token validation and blacklist check
       

        # Your existing logic for staff management
        staff_email = request.data.get('staff_email', '')
        role = request.data.get('role', [])
        staff_name = request.data.get('staff_name', '')

        if not staff_email or not role:
            return Response({
                'message': 'Staff email and role are required for staff management',
            }, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            user.staff_email = staff_email
            # user.role.set(role)
            user.role = role
            user.staff_name = staff_name
            user.save()

        return Response({
            'message': 'Staff setup successfully completed',
            # 'details': UserSerializer(user).data
        }, status=status.HTTP_200_OK)

    return Response({
        'message': 'Invalid request method',
    }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signout_api(request):
    user = request.user

    try:
      
        token = Token.objects.get(user=user)

        # Delete the token
        token.delete()

        
        
        user.save()

        return Response({'detail': 'Successfully signed out.',
                         "name":UserSerializer(user).data['name']}
                         , status=status.HTTP_200_OK)

    except :
        return Response({'detail': 'Error during sign-out.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def roomsetup(request):
    serializer = Roomserializer(data=request.data)
    if serializer.is_valid():
        room_type = serializer.validated_data['room_types']
        room_number = serializer.validated_data['room_number']

        # Assuming you have a user object, replace 'user_instance' with the authenticated user
        user_instance = request.user

        # Create a Roomdata instance
        room_instance = Roomdata.objects.create(room_types=room_type, total_rooms=user_instance, room_number=room_number)

        # Get all rooms associated with the user
        user_rooms = Roomdata.objects.filter(total_rooms=user_instance)

        # Serialize the rooms
        room_serializer = Roomserializer(user_rooms, many=True)

        response_data = {
            "message": "Room created successfully",
            
                
                "total_rooms": room_serializer.data,
                
            
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


