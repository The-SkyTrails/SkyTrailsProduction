from django.views.generic import CreateView , ListView , UpdateView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,logout, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import EnquiryForm,FAQForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


def agent_dashboard(request):
     return render(request,"Agent/Base/index2.html")

def agent_login(request):
    error_message = None  # Initialize the error message as None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('type')
        print("type", user_type, username, password)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if (user_type == "Agent" and user.user_type == "4") or (user_type == "OutSourcing Agent" and user.user_type == "5"):
                auth_login(request, user)
                print("Logged in successfully")
                return redirect('agent_dashboard')  # Redirect to the common dashboard
            else:
                error_message = "User type and user do not match."
        else:
            error_message = "Username or password is incorrect."

    return render(request, 'Agent/LoginPage/newlogin.html', {'error_message': error_message})

class AgentEnquiryCreateView(CreateView):

    model = Enquiry
    form_class = EnquiryForm
    template_name = 'Agent/Leads/addenquiry.html'
    success_url = reverse_lazy('agent_leads') 
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        user = self.request.user
        messages.success(self.request, 'Enquiry Added Successfully.')
        return super().form_valid(form)  


def agent_leads(request):
    user = request.user
    created_enq = Enquiry.objects.filter(created_by=user)
    if user.is_authenticated:
        # Check if the user is an Agent or Outsourcing Agent
        if user.user_type == '4':
            # If the user is an Agent, filter by assign_to_agent
            enq = Enquiry.objects.filter(assign_to_agent=user.agent)
        elif user.user_type == '5':
            # If the user is an Outsourcing Agent, filter by assign_to_outsourcingagent
            enq = Enquiry.objects.filter(assign_to_outsourcingagent=user.outsourcingagent)
        else:
            # Handle other user types as needed
            enq = None
        combined_enq = enq | created_enq
        print("enquiry", combined_enq)

        return render(request, 'Agent/Leads/leads.html', {'enq': combined_enq})

def agent_logout(request):
    logout(request)
    return redirect("agent_login")

  
class appointment_list(ListView):
    model = Appointment
    template_name = 'Agent/Appointment/appointmentlist.html'
    context_object_name = 'appointment'
    
    
class FAQCreateView(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'Agent/FAQ/addfaq.html'
    success_url = reverse_lazy('Agent_faqlist') 
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        messages.success(self.request, 'FAQ Added Successfully.')
          
        return super().form_valid(form)
    
class FAQListView(ListView):
    model = FAQ
    template_name = 'Agent/FAQ/faqlist.html'
    context_object_name = 'FAQs'

class FAQUpdateView(LoginRequiredMixin,UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'Agent/FAQ/updatefaq.html'  
    success_url = reverse_lazy('Agent_faqlist')

    def form_valid(self, form):

        # Display a success message
        messages.success(self.request, 'FAQ updated successfully.')

        return super().form_valid(form)
    
def delete_faq(request, id):
    faq = get_object_or_404(FAQ, id=id)
    faq.delete()
    return redirect('Agent_faqlist')
    