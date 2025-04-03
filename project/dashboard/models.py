from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    # Extends the built-in User model with additional fields.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_number = models.CharField(max_length=20)
    country_code = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    filtering_id = models.IntegerField()  # Typically this would link to an Account Holder's id.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client} - {self.appointment_datetime}"
