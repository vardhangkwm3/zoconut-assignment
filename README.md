# Client Appointment Dashboard

This is a Django-based dashboard for managing clients and their appointments.

## Features

- View clients added in the last two months
- Add new clients via modal
- View client-specific appointments

## Setup Instructions

1. **Install dependencies**  
   Make sure you have Python and Django installed. Install project dependencies using:
   ```bash
   pip install -r requirements.txt
   
2. Run migrations
   python manage.py migrate
   
3. Create a Superuser
   python manage.py createsuperuser

4. Add clients and appointments

    Login to the Django admin panel (/admin/) using the superuser credentials.
    Create clients and their corresponding appointments with the correct account holder ID.
    This ensures that the appointments are properly reflected in the "View Appointments" section of the dashboard.

5. Run the server
   python manage.py runserver

Notes
All appointments must be linked to the respective client account for them to appear correctly in the dashboard.
