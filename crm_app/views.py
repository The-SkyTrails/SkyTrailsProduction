import requests
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils import timezone
from .models import LoginLog 
# Create your views here.





class DashboardView(TemplateView):
    template_name = "SuperadminDashboard/index2.html"

class TravelDashboard(TemplateView):
    template_name = "dashboard/index2.html"


# class CustomLoginView(LoginView):
#     template_name = 'account/login.html'
#     authentication_form = LoginForm

#     def get_success_url(self):
       

#         user_type = self.request.user.user_type
#         if user_type == '1':
            
#             return '/crm/dashboard/'  # Replace with your HOD dashboard URL
        
#         elif user_type == '2':
            
#             return '/Admin/Admindashboard/'  # Replace with your Travel dashboard URL
       
#         else:
#             return '/default_dashboard/'  # Default dashboard URL
        


class CustomLoginView(LoginView):
    template_name = 'account/newlogin.html'
    authentication_form = LoginForm

    def get_public_ip(self):
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            data = response.json()
            return data['ip']
        except Exception as e:
            # Handle the exception (e.g., log the error)
            return None

    def get_success_url(self):
        user_type = self.request.user.user_type

        # Capture the client's public IP address
        public_ip = self.get_public_ip()

        # Create a login log entry with the public IP address
        LoginLog.objects.create(
            user=self.request.user,
            ip_address=public_ip if public_ip else None,
            login_datetime=timezone.now(),
            # date = timezone.now()
        )

        if user_type == '1':
            # return reverse('crm_dashboard')  # Use the URL name for HOD dashboard
            return '/crm/dashboard/'
        
        elif user_type == '2':
            # return reverse('admin_dashboard')  # Use the URL name for Admin dashboard
            return '/Admin/Admindashboard/'

       
        else:
            return ('default_dashboard')  # Use the URL name for the default dashboard
            # return HttpResponse()


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def Error404(request, exception):
    return render(request,'404.html')
