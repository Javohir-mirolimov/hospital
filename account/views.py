from django.shortcuts import render
from main.models import User
from main.serializers import UserSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated






@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                tokens = get_tokens_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': tokens,
                }
            else:
                status = 403
                message = "Invalid Password or Username!"
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined! '
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def singup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    avatar = request.POST.get('avatar')
    phone_number= request.FILES.get('phone_number')
    age = region.POST.get('age')
    password_series = region.POST.get('password_series')
    gender = region.POST.get('gender')
    address = region.POST.get('address')

    new = User.objects.create_user(
        username=username,
        password=password,
        avatar=avatar,
        phone_number = phone_number,
        age=age,
        password_series=password_series,
        gender =gender,
        address=address,

    )
    ser = UserSerializres(new)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data': 'sucses'})


@api_view(['PUT'])
def edit_user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            avatar = request.POST.get('avatar')
            phone_number = request.FILES.get('phone_number')
            age = region.POST.get('age')
            password_series = region.POST.get('password_series')
            gender = region.POST.get('gender')
            address = region.POST.get('address')
            if username is not None:
                user.username = username
            if password is not None:
                user.set_password(password)
            if avatar is not None:
                user.avatar = avatar
            if phone_number is not None:
                user.phone_number = phone_number
            if age is not None:
                user.age = age
            if password_series is not None:
                user.password_series = password_series
            if gender is not None:
                user.gender = gender
            if address is not None:
                user.address_id = address


            user.save()
            ser = UserSerializers(user)
            return Response(ser.data)
        except:
            status = 404
            message = "Request failed"
            data = {
                'status': status,
                'message': message,
            }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        data = {
            'message': "User deleted successfully"
        }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)
