from datetime import *
from re import I
from django.utils import timezone
from django.db import models
from django.db.models import AutoField, BigAutoField
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2, help_text = "Number of available seats")
    rem = models.DecimalField(decimal_places=0, max_digits=2, help_text = "Number of remaining seats")
    price = models.DecimalField(decimal_places=2, max_digits=6,help_text = "Price per seat")
    date = models.DateField(blank=True, null=True,default="2004-09-23",help_text = "Date of departure")
    time = models.TimeField(help_text = "Time of departure")

    def __str__(self):
        return str(self.bus_name)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return str(self.email)


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    cost=models.IntegerField()
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField(blank=True, null=True,default="2004-09-23",help_text="Date of travel")
    time = models.TimeField(help_text="Time of bus")
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return str(self.email)

