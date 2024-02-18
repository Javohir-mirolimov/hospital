from django.urls import path
from .views import *

urlpatterns=[
    #--------------Start  Crud  Employee Model ----------------
    path('get-employee/', GetEmployee.as_view()),
    path('create-employee/', CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployee.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployee.as_view()),
    #---------------Start Crud Revenue Model--------------------
    path('get-revenue/', GetRevenue.as_view()),
    path('create-revenue/', CreateRevenue.as_view()),
    path('update-revenue/<int:pk>/', UpdateRevenue.as_view()),
    path('delete-revenue/int:pk>/', DeleteRevenue.as_view()),
    #-----------------Start Crud Payment Model------------------
    path('get-payment/', GetPayment.as_view()),
    path('create-revenue/', CreatePayment.as_view()),
    path('update-revenue/<int:pk>/', UpdatePayment.as_view()),
    path('delete-revenue/int:pk>/', DeletePayment.as_view()),
    #------------------Start Crud Testimonial_patient Model--------------
    path('get-testimonial-patient/', GetTestimonial_patient.as_view()),
    path('create-testimonial-patient/', CreateTestimonial_patient.as_view()),
    path('update-testimonial-patient/<int:pk>/', UpdateTestimonial_patient.as_view()),
    path('delete-testimonial-patient/int:pk>/', DeleteTestimonial_patient.as_view()),
    #----------------------Start Crud Room Model-----------------------------
    path('get-room/', GetRoom.as_view()),
    path('create-room/', CreateRoom.as_view()),
    path('update-room/<int:pk>/', UpdateRoom.as_view()),
    path('delete-room/int:pk>/', DeleteRoom.as_view()),
    #----------------------Start Crud Patient Model-------------------------
    path('get-patient/', GetPatient.as_view()),
    path('create-patient/', CreatePatient.as_view()),
    path('update-patient/<int:pk>/', UpdatePatient.as_view()),
    path('delete-patient/int:pk>/', DeletePatient.as_view()),
    #---------------------Start Crud About_hospital Model-----------------
    path('get-about-hospital/', GetAboutHospital.as_view()),
    path('create-about-hospital/', CreateAboutHospital.as_view()),
    path('update-about-hospital/<int:pk>/', UpdateAboutHospital.as_view()),
    path('delete-about-hospital/int:pk>/', DeleteAboutHospital.as_view()),
    #---------------------Start Curd Department Model--------------------------
    path('get-department/', GetDepartment.as_view()),
    path('create-department/', CreateDepartment.as_view()),
    path('update-department/<int:pk>/', UpdateDepartment.as_view()),
    path('delete-department/int:pk>/', DeleteDepartment.as_view()),
    #----------------------Start Crud Operation Model----------------------
    path('get-operation/', GetOperation.as_view()),
    path('create-operation/', CreateOperation.as_view()),
    path('update-operation/<int:pk>/', UpdateOperation.as_view()),
    path('delete-operation/int:pk>/', DeleteOperation.as_view()),
    #----------------------Sart Crud Equipment Model----------------------
    path('get-equipment/', GetEquipment.as_view()),
    path('create-equipment/', CreateEquipment.as_view()),
    path('update-equipment/<int:pk>/', UpdateEquipment.as_view()),
    path('delete-equipment/int:pk>/', DeleteEquipment.as_view()),
    #-------------------Start Crud Cassa Model----------------------
    path('get-cassa/', GetCassa.as_view()),
    path('create-cassa/', CreateCassa.as_view()),








]