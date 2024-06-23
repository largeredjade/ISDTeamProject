from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, CustomAuthenticationForm, UserUpdateForm
from .models import Users

class SignUpView(CreateView):
    model = Users
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        password = form.cleaned_data['password']

        user = form.save(commit=False)
        user.set_password(password)
        user.save()

        return super().form_valid(form)



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
    
class UserUpdateView(UpdateView):
    model = Users
    form_class = UserUpdateForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data.get('new_password'):
            user.set_password(form.cleaned_data['new_password'])
        user.save()
        return redirect(self.success_url)
