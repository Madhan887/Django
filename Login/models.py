from tkinter import Widget
from wsgiref import validate
from django.db import models
from django.forms import CharField, DateField, IntegerField, Textarea

# Create your models here.
class createtable(models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.DateField()
    Address=models.TextField()
    Phone=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=10)