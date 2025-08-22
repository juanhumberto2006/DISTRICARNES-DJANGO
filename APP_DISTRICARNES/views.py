from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm   # usa tus formularios
from .models import CustomUser

def index(request):
    return render(request, 'APP_DISTRICARNES/index.html')


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)  # 👈 usamos el login con email
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenido {user.first_name} 👋")
            return redirect('productos')
        else:
            messages.error(request, "Correo o contraseña incorrectos")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'APP_DISTRICARNES/login.html', {"form": form})


def user_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso ✅, ahora puedes iniciar sesión.")
            return redirect('login')
        else:
            messages.error(request, "❌ Revisa los campos, hay errores en el formulario.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'APP_DISTRICARNES/register.html', {"form": form})


@login_required
def pedidos(request):
    return render(request, 'APP_DISTRICARNES/pedidos.html')


@login_required
def productos(request):
    return render(request, 'APP_DISTRICARNES/productos.html')


def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def promociones(request):
    return render(request, 'APP_DISTRICARNES/promociones.html')

@login_required
def contacto(request):
    return render(request, 'APP_DISTRICARNES/contacto.html')

@login_required
def profile(request):
    return render(request, 'APP_DISTRICARNES/profile.html')

@login_required
def edit_profile(request):
    return render(request, 'APP_DISTRICARNES/edit_profile.html')

@login_required
def settings(request):
    return render(request, 'APP_DISTRICARNES/settings.html')
