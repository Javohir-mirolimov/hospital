from django.urls import path
from .views import *

urlpatterns =[
    #-----------------Start Filter Employee Model-------------------
    path('filter_employee_by_fullname/', filter_employee_by_fullname),
    path('filter_employee_by_status/', filter_employee_by_status),
    path('filter_employee_by_time/', filter_employee_by_time),
    path('filter_employee_by_experience/', filter_employee_by_experience),
    path('filter_employee_by_department/', filter_employee_by_department),

]