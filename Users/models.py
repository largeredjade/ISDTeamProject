from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_address = models.CharField(max_length=50)
    user_phoneNumber = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_role = models.CharField(max_length=50)
    user_enterYear = models.DateTimeField()

    def __str__(self):
        return self.user_name
