from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .models import *
from .serializers import *


""" Start Filter Model """
#<<<<<<<<<<<<<<<<<<Start Filter Epployee>>>>>>>>>>>>>>>>

@api_view(['GET'])
def filter_employee_by_fullname(request):
    fullname = request.GET.get('fullname')
    employee = Employee.objects.filter(fullname__icontains=fullname)
    ser = EmployeeSerializers(employee, many=True)

    return Response(ser.data)

@api_view(['GET'])
def filter_employee_by_status(request):
    status = request.GET.get('status')
    employee = Employee.objects.filter(status__icontains=status)
    ser = EmployeeSerializers(employee, many=True)
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
        return Response(ser.data)
    except:
        status = 404
        message = "Employee not found"
        data = {
            'status': status,
            'message': message
        }

@api_view(['GET'])
def filter_employee_by_salary(request):
    salary_str = request.GET.get('salary')
    salary = float(salary_str.replace(',', '.'))
    employee = Employee.objects.filter(salary=salary)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_employee_by_room(request):
    room = request.GET.get('room')
    employee = Employee.objects.filter(room=room)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


#<<<<<<<<<<<<<<<<<<End Filter Epployee>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Patient Filter>>>>>>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_patient_by_doctor(request):
    doctor = request.GET.get('doctor')
    patient = Patient.objects.filter(doctor=doctor)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_patient_by_fullname(reqeust):
    fullname = reqeust.GET.get('fullname')
    patient = Patient.objects.filter(fullname__icontains=fullname)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_patient_by_type_payment(request):
    type_payment = request.GET.get('type_payment')
    patient = Patient.objects.filter(type_payment_iocntains=type_payment)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_gander(request):
    gender = request.GET.get('gender')
    patient = Patient.objects.filter(gender_icontains=gender)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    patient = Patient.objects.filter(phone_number=phone_number)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_patient_by_room(reqeust):
    room = reqeust.GET.get('room')
    patient = Patient.objects.filter(room=room)
    ser = PatientSerializers(patient, many=True)
    return Response(ser.data)

#<<<<<<<<<<<<<<<<End Patient Filter>>>>>>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<Start Room Filter>>>>>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_room_by_name(request):
    name = request.GET.get('name')
    room = Room.objects.filter(name__icontains=name)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_room_by_department(request):
    department = request.GET.get('department')
    room = Room.objects.filter(department=department)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_room_by_capacity(request):
    capacity = request.GET.get('capacity')
    room = Room.objects.filter(capacity=capacity)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_room_by_status(request):
    status = request.GET.get('status')
    room = Room.objects.filter(status__icontains=status)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_room_by_booked_room(reuqest):
    room = Room.objects.filter(booked_room=True)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)


#<<<<<<<<<<<<<<<<End Room Filter>>>>>>>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<Start Payment Filter>>>>>>>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_payment_by_patient(reuqest):
    patient = reuqest.GET.get('patient')
    payment = Payment.objects.filter(patient=patient)
    ser = PaymentSerializers(payment, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_create_at(request):
    create_at = request.GET.get('create_at')
    payment = Payment.objects.filter(create_at=create_at)
    ser = PaymentSerializers(payment, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_payment_by_payment_type(request):
    payment_type = request.GET.get('payment_type')
    payment = Payment.objects.filter(payment_type__icontains=payment_type)
    ser = PaymentSerializers(payment, many=True)
    return Response(ser.data)

#<<<<<<<<<<<<<<<<End Payment Filter>>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<Start Testimonial_patient Filter>>>>>>>>>>>>>>
@api_view(['GET'])
def fiter_testimonial_patient_by_status(request):
    type_testimonial = request.GET.get('type_testimonial')
    testimonial_patient = Testimonial_patient.objects.filter(type_testimonial__icontains=type_testimonial)
    ser = Testimonial_patientSerializers(testimonial_patient, many=True)
    return Response(ser.data)



#<<<<<<<<<<<<<<<<End Testimonial_patient Filter>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Ravenue Filter>>>>>>>>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_ravenue_by_amount(reuqest):
    amount_str = request.GET.get('amount')
    amount = float(salary_str.replace(',', '.'))
    ravenue = Revenue.objects.filter(amount=amount)
    ser = RevenueSerializers(ravenue, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_ravenue_by_create_at(request):
    create_at = request.GET.get('create_at')
    ravenue = Revenue.objects.filter(create_at=create_at)
    ser = PaymentSerializers(ravenue, many=True)
    return Response(ser.data)

#<<<<<<<<<<<<<<<<<End Ravenue Filter>>>>>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Operation Filter>>>>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_operation_by_employee(request):
    doctor = request.GET.get('doctor')
    operation = Operation.objects.filter(doctor__icontains=doctor)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_operation_by_date_time(reuqest):
    date_time = reuqest.GET.get('date_time')
    operation = Operation.objects.filter(date_time=date_time)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_operation_by_time(request):
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    if start_time and end_time:
        filtered_operation = Operation.objects.filter(start_time__gte=start_time, end_time__lte=end_time)
        for operation in filtered_operation:
            print(operation)
        ser = OperationSerializers(filtered_operation, many=True)
        return Response(ser.data)
    else:
        return Response({"error": "Both start_time and end_time are required."}, status=400)


@api_view(['GET'])
def filter_operation_by_patient(request):
    patient = request.GET.get('patient')
    operation = Operation.objects.filter(patient=patient)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_operation_by_room(request):
    room = request.GET.get('room')
    operation = Operation.objects.filter(room=room)
    ser = OperationSerializers(operation, many=True)
    return Response(ser.data)


#<<<<<<<<<<<<<<<<<End Operation Filter>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<Start Equipment Filter>>>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_equipment_by_name(reuqest):
    name = reuqest.GET.get('name')
    equipment = Equipment.objects.filter(name__icontains=name)
    ser = EmployeeSerializers(equipment, many=True)
    return Response(ser.data)


#<<<<<<<<<<<<<<<<<End Equipment Filter>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<<Start Department Filter>>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_department_by_name(reuqest):
    name = reuqest.GET.get('name')
    department = Department.objects.filter(name__icontains=name)
    ser = DepartmentSerializers(department, many=True)
    return Response(ser.data)


#<<<<<<<<<<<<<<<<<<End Department Filter>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<<Start Attendance Filter>>>>>>>>>>>>>>>
@api_view(['GET'])
def filter_attendance_by_employee(request):
    employee = request.GET.get('employee')
    attendance = Attendance.objects.filter(employee=employee)
    ser = AttendanceSerializers(attendance, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_attendance_by_date(request):
    date = request.GET.get('date')
    attendance = Attendance.objects.filter(date=date)
    ser = AttendanceSerializers(attendance, many=True)
    return Response(ser.data)

#<<<<<<<<<<<<<<<<<<End Attendance Filter>>>>>>>>>>>>>>>>>


""" End Filter Model """