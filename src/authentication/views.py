from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from . import forms

def login(request):
    if not request.user.is_authenticated:
        form = forms.LoginForm()
        message = ''
        
        if request.method == 'POST':
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                if user is not None:
                    auth_login(request, user)
                    message = f'Hello {user.username}! You have been logged in'
                    request.session['message'] = message
                    return redirect("dashboard_index")
                else:
                    message = 'Login failed!'
        return render(request, 'login.html', context={'form': form, 'message': message})
    else:
        return redirect('dashboard_index')

@login_required
def logout(request):
    auth_logout(request)
    message = f'Hello ! You have been disconnected'
    request.session['message'] = message
    # return redirect("login", context={'message': message})
    return redirect('login')


def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password2"]
                user = authenticate(username=username, password=password)
                auth_login(request, user)
                messages.success(request, ("Registration successful"))
                return redirect("/user/settings/")
        
        else:
            form = UserCreationForm()

        return render(request, 'register.html', {
            "form": form,
        })
    else:
        return redirect('login')