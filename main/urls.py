from django.urls import path
from .views import *

urlpatterns =[
    #-----------------Start Filter Employee Model-------------------
    path('filter_employee_by_fullname/', filter_employee_by_fullname),
    path('filter_employee_by_status/', filter_employee_by_status),
    path('filter_employee_by_time/', filter_employee_by_time),
    path('filter_employee_by_experience/', filter_employee_by_experience),
    path('filter_employee_by_department/', filter_employee_by_department),
    path('filter_employee_by_salary/', filter_employee_by_salary),
    path('filter_employee_by_room/', filter_employee_by_room),
    path('filter_employee_by_room/', filter_employee_by_room),
    #----------------Start Filter Patient Model-----------------------
    path('filter_patient_by_fullname/', filter_patient_by_fullname),
    path('filter_patient_by_doctor/', filter_patient_by_doctor),
    path('filter_patient_by_type_payment/', filter_patient_by_type_payment),
    path('filter_patient_by_gander/', filter_patient_by_gander),
    path('filter_patient_by_phone_number/', filter_patient_by_phone_number),
    path('filter_patient_by_room/', filter_patient_by_room),
    #---------------Start Filter Room Model-------------------------------
    path('filter_room_by_name/', filter_room_by_name),
    path('filter_room_by_department/', filter_room_by_department),
    path('filter_room_by_capacity/', filter_room_by_capacity),
    path('filter_room_by_status/', filter_room_by_status),
    path('filter_room_by_booked_room/', filter_room_by_booked_room),
    #---------------Start Filter Payment Model------------------------------
    path('filter_payment_by_patient/', filter_payment_by_patient),
    path('filter_payment_by_create_at/', filter_payment_by_create_at),
    #----------------Start Filter Testimonial_patinet Model--------------------------
    path('fiter_testimonial_patient_by_status/', fiter_testimonial_patient_by_status),
    #----------------Start Filter Ravenue Model-----------------------------------
    path('filter_ravenue_by_amount/', filter_ravenue_by_amount),
    path('filter_ravenue_by_create_at/', filter_ravenue_by_create_at),
    #----------------Start Filter Operation Model--------------------------------
    path('filter_operation_by_employee/', filter_operation_by_employee),
    path('filter_operation_by_date_time/', filter_operation_by_date_time),
    path('filter_operation_by_time/', filter_operation_by_time),
    path('filter_operation_by_patient/', filter_operation_by_patient),
    path('filter_operation_by_room/', filter_operation_by_room),
    #------------------Start Filter Equipment Model-----------------------------
    path('filter_equipment_by_name/', filter_equipment_by_name),
    #-----------------Start Filter Department Model----------------------------
    path('filter_department_by_name/', filter_department_by_name),
    #-----------------Start Filter Attendance Model----------------------------
    path('filter_attendance_by_employee/', filter_attendance_by_employee),
    path('filter_attendance_by_date/', filter_attendance_by_date)



]