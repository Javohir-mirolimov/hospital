from django.urls import path
from .views import *

urlpatterns=[
    #--------------Start  Curd  Employee Model ----------------
    path('get-employee/', GetEmployee.as_view()),
    path('create-employee/', CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployee.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployee.as_view()),

]