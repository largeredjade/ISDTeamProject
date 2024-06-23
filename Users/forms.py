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

class UserUpdateForm(forms.ModelForm):
    new_password = forms.CharField(required=False, widget=forms.PasswordInput(), label='New Password')
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = Users
        fields = ['user_id', 'user_address', 'user_phoneNumber', 'user_email', 'user_name', 'user_role', 'user_enterYear']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['user_email'].disabled = True
        self.fields['user_enterYear'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        new_password = self.cleaned_data.get("new_password")
        
        if new_password:
            user.set_password(new_password)

        if commit:
            user.save()
        
        return user