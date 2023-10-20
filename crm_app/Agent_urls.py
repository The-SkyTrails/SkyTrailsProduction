
from django.urls import path , include
from .AdminViews import *
from .AgentViews import *


urlpatterns = [
    
    # path('Dashboard/', TemplateView.as_view(template_name='Agent/Base/index2.html'), name='agent_dashboard'),
    path('Dashboard',agent_dashboard,name="agent_dashboard"),
    path('Login/', agent_login,name="agent_login"),
    
    path('AddLeads/', AgentEnquiryCreateView.as_view(),name="add_leads"),
    path('AllLeads/', agent_leads,name="agent_leads"),

    path('AppointmentList/',appointment_list.as_view(),name="appointment_list"),
    path('Agent/logout', agent_logout,name="agent_logout"),
    
    path('Agent/Addfaq/', FAQCreateView.as_view(),name="Agent_addfaq"),
    path('Agent/faqMaster/', FAQListView.as_view(),name="Agent_faqlist"),
    path('Agent/faqEdit/<int:pk>', FAQUpdateView.as_view(),name="Agent_edit_faq"),
    path('Agent/faq/delete/<int:id>/', delete_faq, name='Agent_delete_faq'),

]