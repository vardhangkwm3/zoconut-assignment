from django.db import models
from django.contrib.auth.models import User

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_number = models.CharField(max_length=20)
    country_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class ClientAppointment(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='appointments')
    appointment_datetime = models.DateTimeField()
    account_holder_id = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.client} on {self.appointment_datetime}"
