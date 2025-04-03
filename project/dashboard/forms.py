from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ClientForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    primary_number = forms.CharField(max_length=20)
    country_code = forms.CharField(max_length=5)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(ClientForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                primary_number=self.cleaned_data['primary_number'],
                country_code=self.cleaned_data['country_code']
            )
        return user
