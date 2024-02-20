from django.urls import path
from .views import singup_view, signin_view, logout_view, edit_user_view, delete_user
urlpatterns =[
    path('create-user/', singup_view),
    path('login-user/', signin_view),
    path('logout-user/', logout_view),
    path('edit-user/<int:pk>/', edit_user_view),
    path('delete-user/<int:pk>/', delete_user),

]
