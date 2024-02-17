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
    avatar = models.ImageField( validators=[(ImageFileValidator)],  verbose_name='hodim_rasmi', upload_to='avatar_photo', null=True, blank=True)
    phone_number = models.CharField(max_length=13,  verbose_name='telefon raqam', unique=True,  validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    age = models.IntegerField( verbose_name='yosh', null=True, blank=True)
    password_series = models.CharField(max_length=255, null=True, blank=True)
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    gender = models.CharField(max_length=25, verbose_name='jinsi', choices=GENDER_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=255,  verbose_name='manzil', null=True, blank=True)
    def __str__(self):
        return self.username


    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Employee(models.Model):
    user = models.ForeignKey(to='User', verbose_name='foydalanuvchi', on_delete=models.CASCADE)
    STARUS_CHOICES = (
        ('director', 'direcotor'),
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('cooker', 'cooker'),
        ('doctor', 'doctor'),
        ('nurse', 'nurse'),
    )
    status = models.CharField(max_length=25, verbose_name='lavozimi',  choices=STARUS_CHOICES)
    experience = models.IntegerField(verbose_name='tajribasi')
    bio = models.TextField(verbose_name="o'zi haqida ma'lumot")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='oylik')
    start_time = models.TimeField(verbose_name='ish boshlash vaqti')
    end_time = models.TimeField(verbose_name='ish tugatish vaqti')
    department = models.ForeignKey(to='Department',  verbose_name="bo'lim" ,on_delete=models.PROTECT)
    room = models.ForeignKey(to='Room', verbose_name='xona' ,on_delete=models.PROTECT)
    create_at = models.DateField(auto_now=True , verbose_name='yaratilgan vaqt')

    def __str__(self):
        return self.user.username


class Revenue(models.Model):
    reason = models.CharField(max_length=255, verbose_name='sabab')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='pul')
    create_at = models.DateField(auto_now=True, verbose_name='yaratilgan vaqt')


class Payment(models.Model):
    payer = models.ForeignKey(to='Patient', verbose_name='bemor', on_delete=models.CASCADE)
    receiver = models.ForeignKey(to='Employee', verbose_name='shifokor', on_delete=models.CASCADE)
    PAYMENT_TYPE_CHOICES = (
        ('full paid', 'full paid'),
        ('part paid', 'part paid'),
        ('unpaid', 'unpaid'),
    )
    payment_type = models.CharField(max_length=25,  verbose_name='tolov turi',choices=PAYMENT_TYPE_CHOICES)
    create_at = models.DateField(auto_now=True, verbose_name='yaratishgan vaqt')
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
    patient = models.ForeignKey(to='Patient', verbose_name='bemor', on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('offer', 'offer'),
        ('complaint', 'complaint'),
        ('testimonial', 'testimonial'),
    )
    type_testimonial = models.CharField(max_length=25, verbose_name='izoh turi', choices=TYPE_CHOICES)
    text = models.TextField(verbose_name='izoh')
    create_at = models.DateField(auto_now=True, verbose_name='yaratilgan vaqt')

    def __str__(self):
        return self.patient.fullname


class Room(models.Model):
    name = models.CharField(max_length=25, verbose_name='nomi')
    capacity = models.IntegerField(verbose_name='sigimi')
    STATUS_CHOICES = (
        ('lux', 'lux'),
        ('econom', 'econom'),
        ('other', 'ther'),
    )
    status = models.CharField(max_length=24, choices=STATUS_CHOICES)
    booked_room = models.BooleanField(default=False, verbose_name=' xona bosh va banligi')


    CAPACITY_STATUS_CHOICES = (
        ('fre', 'free'),
        ('booked', 'booked'),
    )
    capacity_status = models.CharField(max_length=25, verbose_name='capacity_status', choices=CAPACITY_STATUS_CHOICES)
    department = models.ForeignKey(to='Department',  verbose_name='bolim', on_delete=models.PROTECT)
    other_info = models.TextField(verbose_name='malomot')

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
    create_at = models.DateField(auto_now=True, verbose_name='yaratilgan vaqt')

    def __str__(self):
        return self.fullname



class About_hospital(models.Model):
    name = models.CharField(max_length=55, verbose_name='nomi')
    address = models.CharField(max_length=55, verbose_name='manzil')
    email = models.EmailField(validators=[(EmailValidator)], verbose_name='elektiron manzil')
    number_doctor = models.IntegerField(verbose_name='shifokor soni')
    happy_patient = models.IntegerField(verbose_name='hursand bemor')
    reting = models.FloatField(default=0, verbose_name='reting')
    open_data = models.DateField(verbose_name='ochilgan vqat')
    desctiption = models.CharField(max_length=255, verbose_name='tarif')
    motto = models.CharField(max_length=55, verbose_name='shiyor')

    def __str__(self):
        return self.name




class Department(models.Model):
    name = models.CharField(max_length=25, verbose_name='nomi')


    def __str__(self):
        return self.name


class Operation(models.Model):
    doctors = models.ManyToManyField(to='Employee', verbose_name='xodim')
    start_time = models.DateField(verbose_name='aperatsi boshlanosh vaqti ')
    end_time = models.DateField(verbose_name='aperatsi tugash vaqti ')
    patient = models.ForeignKey(to='Patient', verbose_name= 'bemor', on_delete=models.CASCADE)
    room = models.ForeignKey(to='Room', on_delete=models.SET_NULL,  verbose_name='xona',null=True)
    create_at = models.DateField(auto_now=True, verbose_name='yaratilgan b-vaqt')

    def __str__(self):
        return self.patient.fullname




class Equipment(models.Model):
    name = models.CharField(max_length=55, verbose_name='ism')
    rooms = models.ManyToManyField(to='Room', verbose_name='xona')
    number = models.IntegerField(verbose_name='soni')
    extra_info = models.TextField(verbose_name='malumot')

    def __str__(self):
        return self.name

class Casse(models.Model):
    total_amount = models.DecimalField(max_digits=10, verbose_name='pul', decimal_places=2)


