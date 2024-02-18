from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from main.models import *
from main.serializers import *


""" Start Crud Model """


#<<<<<<<<<<<<<<< Start Crud Employee>>>>>>>>>>>>>>>>>
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

#<<<<<<<<<<<<<< End Crud Employee>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<< Start Crud Revenue>>>>>>>>>>>>>>>>
class GetRevenue(ListAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializres

class CreateRevenue(ListCreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializres


class UpdateRevenue(UpdateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializres

class DeleteRevenue(DestroyAPIView):
    queryset = Revenue.objects.all()
    serializer_class = Revenue

#<<<<<<<<<<<<<< End Crud Revenue>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<< Start Crud Payment>>>>>>>>>>>>>>
class GetPayment(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializres

class CreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializres

class UpdatePayment(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializres

class DeletePayment(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializres

#<<<<<<<<<<<<<< End Crud Payment>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<Start Curd Testimonial_patient>>>>>>>>>>>
class GetTestimonial_patient(ListAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializres


class CreateTestimonial_patient(ListCreateAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patient


class UpdateTestimonial_patient(UpdateAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patient

class DeleteTestimonial_patient(DestroyAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializres

#<<<<<<<<<<<<<<End Curd Testimonial_patient>>>>>>>>>>>

#<<<<<<<<<<<<<<<Start Crud Room>>>>>>>>>>>>>>>>>>>>>
class GetRoom(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres

class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres

class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres

class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres

#<<<<<<<<<<<<<<<End Crud Room>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Curd  Patient >>>>>>>>>>>>>>>>>

class GetPatient(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializres

class CreatePatient(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializres

class UpdatePatient(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializres

class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializres
#<<<<<<<<<<<<<<<<<End Curd  Patient >>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<< Start Crud About_Hospital>>>>>>>>>>>>
class GetAboutHospital(ListAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializres


class CreateAboutHospital(ListCreateAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializres


class UpdateAboutHospital(UpdateAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializres


class DeleteAboutHospital(DestroyAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializres

#<<<<<<<<<<<<<<<<< End Crud About_Hospital>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Crud Department>>>>>>>>>>>>>>>
class GetDepartment(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializres


class CreateDepartment(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializres


class UpdateDepartment(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializres


class DeleteDepartment(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializres

#<<<<<<<<<<<<<<<<<End Crud Department>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Crud Operation>>>>>>>>>>>>>>
class GetOperation(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializres


class CreateOperation(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializres


class UpdateOperation(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializres


class DeleteOperation(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializres

#<<<<<<<<<<<<<<<<<End Crud Operation>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<Start Crud Equipment>>>>>>>>>>>>
class GetEquipment(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EmployeeSerializres


class CreateEquipment(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EmployeeSerializres


class UpdateEquipment(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EmployeeSerializres


class DeleteEquipment(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EmployeeSerializres

#<<<<<<<<<<<<<<<<End Crud Equipment>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Crud Cassa>>>>>>>>>>>>>>>
class GetCassa(ListAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializres


class CreateCassa(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializres


#<<<<<<<<<<<<<<<<<End Crud Cassa>>>>>>>>>>>>>>>

""" End Crud Model """

