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
    phone_number = request.POST.get('phone_number')
    avatar = request.FILES.get('avatar')
    age = region.POST.get('age')
    state = region.POST.get('state')
    region = region.POST.get('region')
    addres_street = region.POST.get('addres_street')
    sex = region.POST.get('sex')
    nationality = region.POST.get('nationality')
    password_series = region.POST.get('password_series')
    status = region.POST.get('status')
    new = User.objects.create_user(
        username=username,
        password=password,
        phone_number=phone_number,
        age = age,
        state=state,
        region =region,
        sex =sex,
        nationality =nationality,
        password_series =password_series,
        status = status,
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
            username = request.data.get('username')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            address = request.data.get('address')
            phone_number = request.data.get('phone_number')
            password = request.data.get('password')
            age = region.data.get('age')
            state = region.data.get('state')
            region = region.data.get('region')
            addres_street = region.data.get('addres_street')
            sex = region.data.get('sex')
            nationality = region.data.get('nationality')
            password_series = region.data.get('password_series')
            status = region.data.get('status')
            if username is not None:
                user.username = username
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.last_name = last_name
            if email is not None:
                user.email = email
            if address is not None:
                user.address_id = address
            if phone_number is not None:
                user.phone_number = phone_number
            if password is not None:
                user.set_password(password)
            if age is not None:
                user.age = age
            if state is not None:
                user.state = state
            if region is not None:
                user.region = region
            if addres_street is not None:
                user.addres_street = addres_street
            if sex is not None:
                user.sex = sex
            if nationality is not None:
                user.nationality = nationality
            if password_series is not  None:
                user.password_series = password_series
            if status is not None:
                user.status = status
            user.save()
            ser = UserSerializer(user)
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
