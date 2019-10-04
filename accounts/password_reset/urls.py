from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset/home.html'
         ),
         name='password_reset'),
]
