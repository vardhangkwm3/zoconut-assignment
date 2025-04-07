from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import login, logout
from .models import ClientProfile, ClientAppointment
from .forms import ClientForm

@login_required
def dashboard_home(request):
    account_holder_id = request.user.id

    # Define the time window (last 2 months)
    two_months_ago = timezone.now() - timedelta(days=60)

    new_clients_count = ClientProfile.objects.filter(timestamp__gte=two_months_ago).count()
    new_appointments_count = ClientAppointment.objects.filter(
        appointment_datetime__gte=two_months_ago,
        account_holder_id=account_holder_id
    ).count()

    # fetching Client...
    clients = ClientProfile.objects.filter(timestamp__gte=two_months_ago)

    context = {
        'new_clients_count': new_clients_count,
        'new_appointments_count': new_appointments_count,
        'clients': clients,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Return form errors as JSON.
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def logging_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('dashboard:dashboard')

@login_required
def appointments_list(request):
    account_holder_id = request.user.id
    # Get appointments for the account holder from the last 2 months (for example)
    two_months_ago = timezone.now() - timedelta(days=60)
    appointments = ClientAppointment.objects.filter(
        account_holder_id=account_holder_id,
        appointment_datetime__gte=two_months_ago
    ).order_by('appointment_datetime')
    
    context = {
        'appointments': appointments,
    }
    return render(request, 'dashboard/appointments.html', context)

@login_required
def update_appointment_status(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        new_status = request.POST.get('status')
        try:
            appointment = ClientAppointment.objects.get(id=appointment_id, account_holder_id=request.user.id)
            # Optionally, validate that new_status is one of the allowed values
            if new_status in dict(ClientAppointment.STATUS_CHOICES):
                appointment.status = new_status
                appointment.save()
                return JsonResponse({'success': True, 'new_status': appointment.status})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid status value.'})
        except ClientAppointment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Appointment not found.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})
