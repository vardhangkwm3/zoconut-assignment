from django import forms
from django.contrib.auth.models import User
from .models import ClientProfile

class ClientForm(forms.ModelForm):
    # Form fields for both User and ClientProfile
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = ClientProfile
        fields = ['primary_number', 'country_code']

    def save(self, commit=True):
        # Create a new User instance first.
        user_data = {
            'username': self.cleaned_data['username'],
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'email': self.cleaned_data['email'],
        }
        user = User.objects.create(**user_data)
        client_profile = super().save(commit=False)
        client_profile.user = user
        if commit:
            client_profile.save()
        return client_profile
