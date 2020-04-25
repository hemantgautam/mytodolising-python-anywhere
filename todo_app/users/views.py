from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .forms import UserRegisterForm, UserUpdateForm, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import logout_require


# Create your views here.


@logout_require
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(email="hemantgautam50@gmail.com", password="Krishnita@1")
        if user is not None and user:
            login(request, user)
            return redirect('boards')
        else:
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'users/login.html', {'form': form})


@logout_require
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created. You are ready to login')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context = {
            'u_form': u_form,
            'pr_class': 'active',
        }
        return render(request, 'users/profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            pass
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/profile.html', {
        'pc_form': form,
        'pc_class': 'active',
    })
