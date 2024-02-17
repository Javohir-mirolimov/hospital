from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from . import models



@admin.register(models.User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('avatar', 'phone_number', 'age', 'password_series', 'gender', 'address', )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )



admin.site.register(models.Employee)
admin.site.register(models.Revenue)
admin.site.register(models.Payment)
admin.site.register(models.Testimonial_patient)
admin.site.register(models.Room)
admin.site.register(models.Patient)
admin.site.register(models.About_hospital)
admin.site.register(models.Department)
admin.site.register(models.Operation)
admin.site.register(models.Equipment)
