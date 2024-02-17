from django.db import models
from django.contrib.auth.models import AbstractUser
import re
# import qrсode
# from io import BytesIO
# from django.core.files import File


from django.core.validators import RegexValidator, EmailValidator
from .validators import ImageFileValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    avatar = models.ImageField( validators=[(ImageFileValidator)], upload_to='avatar_photo')
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    age = models.IntegerField()
    password_series = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.username


    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Employee(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    STARUS_CHOICES = (
        ('director', 'direcotor'),
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('cooker', 'cooker'),
        ('doctor', 'doctor'),
        ('nurse', 'nurse'),
    )
    status = models.CharField(max_length=25, choices=STARUS_CHOICES)
    experience = models.IntegerField()
    specialty = models.CharField(max_length=55)
    bio = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    department = models.ForeignKey(to='Department', on_delete=models.PROTECT)
    room = models.ForeignKey(to='Room', on_delete=models.PROTECT)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username


class Revenue(models.Model):
    reason = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateField(auto_now=True)


class Payment(models.Model):
    payer = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    receiver = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    PAYMENT_TYPE_CHOICES = (
        ('full paid', 'full paid'),
        ('part paid', 'part paid'),
        ('unpaid', 'unpaid'),
    )
    payment_type = models.CharField(max_length=25, choices=PAYMENT_TYPE_CHOICES)
    create_at = models.DateField(auto_now=True)
    # def save(self, *args, **kwargs):
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=8,
    #         border=4,
    #     )
    #     qr.add_data(f"Your data to encode in the QR code: {self.user.username}")
    #     qr.make(fit=True)
    #     img = qr.make_image(fill_color="black", back_color="white")
    #     buffer = BytesIO()
    #     img.save(buffer)
    #     buffer.seek(0)
    #
    #     self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
    #
    #     super().save(*args, **kwargs)


class Testimonial_patient(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('offer', 'offer'),
        ('complaint', 'complaint'),
        ('testimonial', 'testimonial'),
    )
    type_testimonial = models.CharField(max_length=25, choices=TYPE_CHOICES)
    text = models.TextField()
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.patient.fullname


class Room(models.Model):
    name = models.CharField(max_length=25)
    capacity = models.IntegerField()
    STATUS_CHOICES = (
        ('lux', 'lux'),
        ('econom', 'econom'),
        ('other', 'ther'),
    )
    status = models.CharField(max_length=24, choices=STATUS_CHOICES)

    CAPACITY_STATUS_CHOICES = (
        ('fre', 'free'),
        ('booked', 'booked'),
    )
    capacity_status = models.CharField(max_length=25, choices=CAPACITY_STATUS_CHOICES)
    department = models.ForeignKey(to='Department', on_delete=models.PROTECT)
    other_info = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    doctor = models.ForeignKey(to='Employee', on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=55)
    address = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    photo = models.ImageField(upload_to='avatar_paient/' ,  validators=[(ImageFileValidator)] , blank=True, null=True)
    bio = models.TextField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    TYPE_PAYMENT_CHOICES = (
        ('offer', 'offer'),
        ('complaint', 'complaint'),
        ('testimonial', 'testimonial'),
    )
    type_payment = models.CharField(max_length=25, choices=TYPE_PAYMENT_CHOICES)
    room = models.ForeignKey(to='Room', on_delete=models.SET_NULL, null=True)
    booked_room = models.BooleanField(default=False)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.fullname



class About_hospital(models.Model):
    name = models.CharField(max_length=55)
    address = models.CharField(max_length=55)
    email = models.EmailField(validators=[(EmailValidator)])
    number_doctor = models.IntegerField()
    happy_patient = models.IntegerField()
    reting = models.FloatField(default=0)
    open_data = models.DateField()
    desctiption = models.CharField(max_length=255)
    motto = models.CharField(max_length=55)

    def __str__(self):
        return self.name




class Department(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name


class Operation(models.Model):
    doctors = models.ManyToManyField(to='Employee')
    start_time = models.DateField()
    end_time = models.DateField()
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    room = models.ForeignKey(to='Room', on_delete=models.SET_NULL, null=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.patient.fullname




class Equipment(models.Model):
    name = models.CharField(max_length=55)
    rooms = models.ManyToManyField(to='Room')
    number = models.IntegerField()
    extra_info = models.TextField()

    def __str__(self):
        return self.name

class Casse(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


