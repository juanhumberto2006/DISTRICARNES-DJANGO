from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'password1', 'password2', 'terms']

# 🔑 Creamos un login basado en email
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Correo", widget=forms.EmailInput(attrs={'autofocus': True}))

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
