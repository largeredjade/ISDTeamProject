from django.contrib import admin
from .models import Users
# Register your models here.
@admin.register(Users)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_address','user_email', 'user_phoneNumber')
