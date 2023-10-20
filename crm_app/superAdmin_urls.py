

from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from .SuperAdminViews import *




urlpatterns = [
    path('logout_user', logout_user,name="logout"),
    path("dashboard/", DashboardView.as_view() , name='dashboard'),
    path('add_admin/', add_admin,name="add_admin"),
    path('view_admin/', view_admin,name="view_admin"),
    
       
]

