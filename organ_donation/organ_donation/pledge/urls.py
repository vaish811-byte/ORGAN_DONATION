
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pledge_view, name='pledge_form'),
    path('donors/', views.donor_list, name='donor_list'),
        path('certificate/<int:donor_id>/', views.generate_certificate, name='generate_certificate'), 
      
    path('recipient/register/', views.recipient_register, name='recipient_register'),
    path('recipient/list/', views.recipient_list, name='recipient_list'),



]
