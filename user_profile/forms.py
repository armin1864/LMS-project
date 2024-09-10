from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'registration_date', 'is_active',
                  'is_staff')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'registration_date',
                  'is_active', 'is_staff')

    def clean_password(self):
        return self.initial['password']
