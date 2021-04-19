from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class AdminRegistration(models.Model):
    # admin_auth = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, null=True)
    password = models.CharField(max_length=30, validators=[MinLengthValidator(4)])
    confrim_password = models.CharField(max_length=30, validators=[MinLengthValidator(4)])
    join = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user_name
    