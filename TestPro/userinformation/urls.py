"""userinformation-urls"""
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('userinfosubmission', views.userinfosubmission, name='userinfosubmission')
]