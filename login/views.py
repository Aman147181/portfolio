from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            thisuser = authenticate(username=username, password=password)
            if thisuser is not None:
                auth_login(request, thisuser)
                return redirect('home')
            else:
                messages.error(request,f'either username or password is invalid!!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
