from django.urls import path
from .views import *

urlpatterns =[
    #-----------------Start Filter Employee Model-------------------
    path('filter_employee_by_fullname/', filter_employee_by_fullname)

]