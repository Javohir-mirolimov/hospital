from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


""" Start Filter Model """
#<<<<<<<<<<<<<<<<<<Start Filter Epployee>>>>>>>>>>>>>>>>

@api_view(['GET'])
def filter_employee_by_fullname(request):
    slug = request.GET.get('slug')
    employee = Employee.objects.filter(slug__icontains=slug)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)





#<<<<<<<<<<<<<<<<<<End Filter Epployee>>>>>>>>>>>>>>>>

""" End Filter Model """