from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
    
class DashboardView(TemplateView):
    template_name = "SuperadminDashboard/index2.html"



def add_admin(request):
    if request.method == "POST":
        department = request.POST.get('department')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        try:
            if CustomUser.objects.filter(username = email).exists():
                messages.warning(request,f"{email} Admin already exists")
                return redirect('add_admin')

            if CustomUser.objects.filter(email = email).exists():
                messages.warning(request,f"{email} This email already exists")
                return redirect('add_admin')
            
            user = CustomUser.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password,user_type='2')
           
            user.admin.department=department
            user.admin.contact_no=contact
            user.save()
            subject = 'Congratulations! Your Account is Created'
            message = f'Hello {firstname} {lastname},\n\n' \
                f'Welcome to SSDC \n\n' \
                f'Congratulations! Your account has been successfully created as an admin.\n\n' \
                f' Your id is {email} and your password is {password}.\n\n' \
                f' go to login : https://crm.theskytrails.com/ \n\n' \
                f'Thank you for joining us!\n\n' \
                f'Best regards,\nThe Sky Trails'  # Customize this message as needed

            # Change this to your email
            recipient_list = [email]  # List of recipient email addresses

            send_mail(subject, message, from_email=None, recipient_list=recipient_list)
            messages.success(request,f"{email} Created Successfully and Congratulatory Email Sent!!!")
            return redirect('view_admin')
        except Exception as e:
            messages.warning(request,'Something is Wrong Try Again')
        
        
        
    return render(request,'SuperadminDashboard/employee/addadmin.html')


def view_admin(request):
    admin=Admin.objects.all()
    context = {
        'admin':admin
    }

    return render(request,'SuperadminDashboard/employee/adminlist.html',context)    