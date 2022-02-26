from email import message
import email
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def Login(request):
    if request.method=='POST':
        Name=request.POST['Name']
        password=request.POST['Password']
        user=auth.authenticate(username=Name,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"content.html")
        else:
            return HttpResponse("Invalid username or password please go back and enter valid username and password")
    return render(request,"index.html")

def Create1(request):
    if request.method =='POST':
        a=createtable()
        a.Name=request.POST.get('Name')
        a.DOB=request.POST.get('DOB')
        a.Address=request.POST.get('Address')
        a.Phone=request.POST.get('Phone')
        a.save()
        Name=request.POST['Name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        CPassword=request.POST['CPassword']

        if Password==CPassword:
            if User.objects.filter(username=Email).exists():
                messages.info(request,'already used')
                return redirect('/create')
            else:
                user=User.objects.create_user(username=Name,password=Password,email=Email)
                user.save()
                return redirect("/Login")
      
        
    return render(request,"create.html")
