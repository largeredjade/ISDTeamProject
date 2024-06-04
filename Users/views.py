from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from .models import Users

class SignUpView(CreateView):
    model = Users
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "html/signup.html"
