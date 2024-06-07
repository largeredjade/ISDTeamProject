from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, CustomAuthenticationForm
from .models import Users

class SignUpView(CreateView):
    model = Users
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)