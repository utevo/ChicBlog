from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    path('register/', accounts_views.register, name='register' ),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
    path('password_reset/', include('accounts.password_reset.urls')),
]
