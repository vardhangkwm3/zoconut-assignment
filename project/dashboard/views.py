from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils import timezone
from datetime import timedelta

from .models import Profile, Appointment
from .forms import ClientForm

@login_required
def dashboard(request):
    account_holder = request.user  # Assuming the logged-in user is the Account Holder
    two_months_ago = timezone.now() - timedelta(days=60)
    
    # Fetch clients added in the last 2 months.
    new_clients = Profile.objects.filter(timestamp__gte=two_months_ago)
    
    # Fetch appointments linked to the account holder (using filtering_id).
    new_appointments = Appointment.objects.filter(timestamp__gte=two_months_ago, filtering_id=account_holder.id)
    
    context = {
        'new_clients_count': new_clients.count(),
        'new_appointments_count': new_appointments.count(),
        'clients': new_clients,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def add_client(request):
    if request.method == 'POST' and request.is_ajax():
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Client added successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseBadRequest("Invalid request")
