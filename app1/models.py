from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    iin = models.CharField(max_length= 50,blank=True, null=True, unique=True)
    surname = models.CharField(max_length= 50, blank=True, null=True)
    name = models.CharField(max_length= 50, blank=True, null=True)
    patronymic = models.CharField(max_length= 50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length= 50, blank=True, null=True)


class Cemetery(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, null=True, blank=True) 
    
    
class BurialPlace(models.Model):
    cemetery = models.ForeignKey(Cemetery, on_delete=models.CASCADE)
    grave_num = models.CharField(max_length=50,  blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    grave_photo = models.CharField(max_length=100, null=True, blank=True)
    is_reserved = models.BooleanField(default=False)
    is_busy = models.BooleanField(default=False)
    
    
class Deceased(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    burial_place = models.OneToOneField(BurialPlace, null=True, blank=True, on_delete=models.SET_NULL)
    death_cause = models.CharField(max_length= 50, blank=True, null=True)
    from_morgue_id = models.CharField(max_length= 50, blank=True, null=True)
    burial_day = models.DateField(blank=True, null=True)
    death_certificate_number = models.CharField(max_length= 50, blank=True, null=True)
    is_buried = models.BooleanField(default=False)
    
    
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    
    
class Application(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    deceased = models.ForeignKey(Deceased, on_delete=models.CASCADE)
    burial_place = models.ForeignKey(BurialPlace, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)








