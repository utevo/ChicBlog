from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'password_reset'

urlpatterns = [
    path('',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset/home.html'
         ),
         name='home'),
    path('done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset/done.html'
         ),
         name='done'),
]
