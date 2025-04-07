from django.contrib import admin
from .models import ClientAppointment, ClientProfile

# Register your models here.

admin.site.register(ClientProfile)
admin.site.register(ClientAppointment)