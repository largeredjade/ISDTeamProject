from django import forms
from .models import Users
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['user_id', 'user_address', 'user_address', 'user_phoneNumber', 'user_email','password', 'user_name', 'user_role', 'user_enterYear']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))
