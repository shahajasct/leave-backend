import email
import requests
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.utils import timezone
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("pword")
        user = auth.authenticate(username = email, password = password)
        if user is None:
            messages.success(request, 'Invalid credentials')
            return render(request, 'login.html')
        auth.login(request, user)
        if Registration.objects.filter(user = user, Password = password).exists():
            logs = Registration.objects.filter(user = user, Password = password)
            for value in logs:
                user_id = value.id
                usertype  = value.User_role
                teacher_email = value.Email
                if usertype == 'admin':
                    request.session['logg'] = user_id
                    print(request.session['logg'])
                   
    return redirect('admin_home')



def leave_register(request):
    a=Registration.objects.get(User_role= 'empolyee')
    if request.method =='POST':
        email = request.POST.get('email')
        description = request.POST.get('descr')
        start_date=request.POST.get('s_date')
        end_date=request.POST.get('end_date')
        return redirect('home')
    return render(request,'leave_portal.html')

def leave_approves(request,id):
    ab=Admin.objects.get(id=id)
    ab.Approval_status='approved'
    ab.save()
    bc=Admin.objects.all()
    return render(request,'home.html',{'bc':bc})