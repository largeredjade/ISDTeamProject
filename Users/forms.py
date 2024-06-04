from django import forms
from .models import Users

class UserRegistrationForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = '__all__'
