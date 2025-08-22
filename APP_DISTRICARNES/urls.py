from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('productos/', views.productos, name='productos'),
    path('promociones/', views.promociones, name='promociones'),
    path('contacto/', views.contacto, name='contacto'),

    # ✅ PERFIL Y CONFIG
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings, name='settings'),

    # ✅ Cambio de contraseña (usando vistas de Django)
    path('password/change/', 
         auth_views.PasswordChangeView.as_view(template_name="APP_DISTRICARNES/change_password.html"), 
         name='change_password'),
    path('password/change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name="APP_DISTRICARNES/change_password_done.html"), 
         name='password_change_done'),
]
