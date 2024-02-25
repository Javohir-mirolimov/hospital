from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import time

from .models import *
from .serializers import *


""" Start Filter Model """
#<<<<<<<<<<<<<<<<<<Start Filter Epployee>>>>>>>>>>>>>>>>

@api_view(['GET'])
def filter_employee_by_fullname(request):
    try:
        slug = request.GET.get('slug')
        employee = Employee.objects.filter(slug__icontains=slug)
        ser = EmployeeSerializers(employee, many=True)
    except:
        status = 404
        message = "Employee not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(ser.data)

@api_view(['GET'])
def filter_employee_by_status(request):
    try:
        status = request.GET.get('status')
        employee = Employee.objects.filter(status__icontains=status)
        ser = EmployeeSerializers(employee, many=True)
    except:
        status = 404
        message = "Employee not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_time(request):
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    if start_time and end_time:
        filtered_employees = Employee.objects.filter(start_time__gte=start_time, end_time__lte=end_time)
        for employee in filtered_employees:
            print(employee)
        ser = EmployeeSerializers(filtered_employees, many=True)
        return Response(ser.data)
    else:
        return Response({"error": "Both start_time and end_time are required."}, status=400)
@api_view(['GET'])
def filter_employee_by_experience(request):
    try:
        experience = request.GET.get('experience')
        employee = Employee.objects.filter(experience=experience)
        ser = EmployeeSerializers(employee, many=True)
    except:
        status = 404
        message = "Employee not found"
        data = {
            'status': status,
            'message': message
        }

    return Response(ser.data)


@api_view(['GET'])
def filter_employee_by_department(request):
    try:
        department = request.GET.get('department')
        employee = Employee.objects.filter(department=department)
        ser = EmployeeSerializers(employee, many=True)
    except:
        status = 404
        message = "Employee not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(ser.data)




#<<<<<<<<<<<<<<<<<<End Filter Epployee>>>>>>>>>>>>>>>>

""" End Filter Model """