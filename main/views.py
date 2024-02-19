from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from main.models import *
from main.serializers import *


"----------START Employee CRUD----------"
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
"----------END Employee CRUD----------"


"----------START Revenue CRUD----------"
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
"----------END Revenue CRUD----------"


"----------START Payment CRUD----------"
class GetPayment(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class CreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers
er
class UpdatePayment(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


class DeletePayment(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers
"----------END Payment CRUD----------"


"----------START Testimonial_patient CRUD----------"
class GetTestimonial_patient(ListAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers


class CreateTestimonial_patient(ListCreateAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers


class UpdateTestimonial_patient(UpdateAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializeer


class DeleteTetimonial_patient(DestroyAPIView):
    queryset = Testimonial_patient.objects.all()
    serializer_class = Testimonial_patientSerializers
"----------END Testimonial_patient CRUD----------"


"----------START Room CRUD----------"
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
"----------END Room CRUD----------"


"----------START Patient CRUD----------"
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
"----------END Patient CRUD----------"


"----------START About_hospital CRUD----------"
class GetAbout_hospital(ListAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers


class CreateAbout_hospital(ListCreateAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers


class UpdateAbout_hospital(UpdateAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers


class DeleteAbout_hospital(DestroyAPIView):
    queryset = About_hospital.objects.all()
    serializer_class = About_hospitalSerializers
"----------END About_hospital CRUD----------"


"----------START Department CRUD----------"
class GetDepartment(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class CreateDepartment(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class UpadteDepartment(UpdateAPIView):
    queryset = Department.obkjects.all()
    serializer_class = DepartmentSerializers


class DeleteDepartment(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
"----------END Department CRUD----------"


"----------START Operation CRUD----------"
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
"----------END Operation CRUD----------"


"----------START Equipment CRUD----------"
class GetEquipment(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers


class CreateEquipment(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers


class UpdateEquipment(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers


class DeletEquipment(DestroyAPIView):
    queryset = Equipment.objectrs.all()
    serializer_class = EquipmentSerializers
"----------END Equipment CRUD----------"


"----------START Cassa CRUD----------"
class GetCassa(ListAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


class CreateCassa(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers
"----------END Cassa CRUD----------"