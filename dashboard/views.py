from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from main.models import *
from main.serializers import *


""" Start Crud Model """


#<<<<<<<<<<<<<<< Start Curd Employee>>>>>>>>>>>>>>>>>
class GetEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres

class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres

class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres

#<<<<<<<<<<<<<< End Curd Employee>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<< Start

""" End Crud Model """

