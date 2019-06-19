from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request, "home.html", {"form":form})

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form":form})
