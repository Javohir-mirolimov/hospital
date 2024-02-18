from rest_framework import serializers
from .models import *


class UserSerializres(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeSerializres(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class RevenueSerializres(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"

class PaymentSerializres(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class Testimonial_patientSerializres(serializers.ModelSerializer):
    class Meta:
        model = Testimonial_patient
        fields = "__all__"

class RoomSerializres(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class PatientSerializres(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class About_hospitalSerializres(serializers.ModelSerializer):
    class Meta:
        model = About_hospital
        fields = "__all__"

class DepartmentSerializres(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class OperationSerializres(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"

class EquipmentSerializres(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"

class CassaSerializres(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"




