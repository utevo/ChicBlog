from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('chicblog:home')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
