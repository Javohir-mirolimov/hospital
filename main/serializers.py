from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class RevenueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class Testimonial_patientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial_patient
        fields = "__all__"

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class About_hospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = About_hospital
        fields = "__all__"

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class OperationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"

class EquipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"

class CassaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"




