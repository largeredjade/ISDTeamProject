from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, user_email, user_name, password=None):
        if not user_email:
            raise ValueError('이메일은 필수입니다.')
        if not user_name:
            raise ValueError('사용자명은 필수입니다.')

        user = self.model(
            user_email=self.normalize_email(user_email),
            user_name=user_name,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, user_email, user_name, password=None):
        user = (self.create_user(
            user_email=user_email,
            user_name=user_name,
            password=password,
        ))
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    user_address = models.CharField(max_length=50)
    user_phoneNumber = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=50, unique=True)
    user_role = models.CharField(max_length=50)
    user_enterYear = models.DateField(null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name
