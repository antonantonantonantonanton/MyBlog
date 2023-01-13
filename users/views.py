from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """New user registration"""
    if request.method != 'POST':
        # Output empty registration form.
        form = UserCreationForm()
    else:
        # Processing the Form Fill.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Logging in and redirecting to the home page.
            login(request, new_user)
            return redirect('blogs:posts')

    # Output an empty or invalid form.
    context = {'form': form}
    return render(request, "registration/register.html", context)