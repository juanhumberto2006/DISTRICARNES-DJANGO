from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    terms = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'   # se usará el correo para login
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
