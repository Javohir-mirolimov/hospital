from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serializers import *


""" Start Crud Model """


#<<<<<<<<<<<<<<< Start Crud Employee>>>>>>>>>>>>>>>>>
class GetEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

#<<<<<<<<<<<<<< End Crud Employee>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<< Start Crud Revenue>>>>>>>>>>>>>>>>
class GetRevenue(ListAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializers

class CreateRevenue(ListCreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializers


class UpdateRevenue(UpdateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializers

class DeleteRevenue(DestroyAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializers

#<<<<<<<<<<<<<< End Crud Revenue>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<< Start Crud Payment>>>>>>>>>>>>>>
class GetPayment(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class CreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class UpdatePayment(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class DeletePayment(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

#<<<<<<<<<<<<<< End Crud Payment>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<Start Curd Testimonial_patient>>>>>>>>>>>
class GetTestimonial_patient(ListAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers


class CreateTestimonial_patient(ListCreateAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers


class UpdateTestimonial_patient(UpdateAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers

class DeleteTestimonial_patient(DestroyAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers

#<<<<<<<<<<<<<<End Curd Testimonial_patient>>>>>>>>>>>

#<<<<<<<<<<<<<<<Start Crud Room>>>>>>>>>>>>>>>>>>>>>
class GetRoom(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

#<<<<<<<<<<<<<<<End Crud Room>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Curd  Patient >>>>>>>>>>>>>>>>>

class GetPatient(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class CreatePatient(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class UpdatePatient(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
#<<<<<<<<<<<<<<<<<End Curd  Patient >>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<< Start Crud About_Hospital>>>>>>>>>>>>
class GetAboutHospital(ListAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers


class CreateAboutHospital(ListCreateAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers


class UpdateAboutHospital(UpdateAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers


class DeleteAboutHospital(DestroyAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers

#<<<<<<<<<<<<<<<<< End Crud About_Hospital>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Crud Department>>>>>>>>>>>>>>>
class GetDepartment(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class CreateDepartment(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class UpdateDepartment(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class DeleteDepartment(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

#<<<<<<<<<<<<<<<<<End Crud Department>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Crud Operation>>>>>>>>>>>>>>
class GetOperation(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class CreateOperation(ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class UpdateOperation(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers


class DeleteOperation(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializers

#<<<<<<<<<<<<<<<<<End Crud Operation>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<Start Crud Equipment>>>>>>>>>>>>
class GetEquipment(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers


class CreateEquipment(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers


class UpdateEquipment(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers


class DeleteEquipment(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers

#<<<<<<<<<<<<<<<<End Crud Equipment>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Crud Cassa>>>>>>>>>>>>>>>
class GetCassa(ListAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


class CreateCassa(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


#<<<<<<<<<<<<<<<<<End Crud Cassa>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<Start Crud Attendance>>>>>>>>>>
class GetAttendance(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class CreateAttendance(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class UpdateAttendance(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers


class DeleteAttendance(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers



#<<<<<<<<<<<<<<<<End Crud Attendance>>>>>>>>>>>

""" End Crud Model """

