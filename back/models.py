from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Registration(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=200)

class Leave_register(models.Model):
    Name=models.CharField(max_length=200)
    Desription=models.TextField()
    Start_date=models.DateField()
    End_date=models.DateField()

class Admin(models.Model):
    Approval_status=models.AutoField()