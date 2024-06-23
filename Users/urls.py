from django.urls import path
from .views import SignUpView, CustomLoginView, UserUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update/', UserUpdateView.as_view(), name='update_profile'),
]
