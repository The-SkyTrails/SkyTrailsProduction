"""TravoltCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import *
from django.views.generic import TemplateView
from crm_app.views import *
from django.views.static import serve
from django.urls import re_path
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),


    path('', CustomLoginView.as_view(), name='login'),
    path("dashboard/", DashboardView.as_view() , name='dashboard'),
    # path('logout_user', logout_user,name="logout"),

    # path('', include('account.urls')),
    path('crm/', include('crm_app.superAdmin_urls')),
    path('Admin/', include('crm_app.Admin_urls')),
    path('Agent/', include('crm_app.Agent_urls')),
    path('Employee/', include('crm_app.Employee_urls')),
    path('country/',TemplateView.as_view(template_name='Admin/agentmanagement/agentupdate.html'),name='country')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'crm_app.views.Error404'

