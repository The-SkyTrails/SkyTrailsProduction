from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "SuperadminDashboard/index2.html"

class TravelDashboard(TemplateView):
    template_name = "dashboard/index2.html"

class CustomLoginView(LoginView):
    template_name = 'account/newlogin.html'
    authentication_form = LoginForm

    def get_success_url(self):
       
        user_type = self.request.user.user_type
        if user_type == '1':
            
            return '/dashboard/'  # Replace with your HOD dashboard URL
        
        elif user_type == '2':
            
            return '/Admindashboard/'  # Replace with your Travel dashboard URL
       
        else:
            return '/default_dashboard/'  # Default dashboard URL
        
