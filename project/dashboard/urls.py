from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('addclient/', views.add_client, name='add_client'),
    path('logout/', views.logging_out, name='logout'),
    path('appointments/', views.appointments_list, name='appointments'),
    path('appointments/update/', views.update_appointment_status, name='update_appointment'),
]
