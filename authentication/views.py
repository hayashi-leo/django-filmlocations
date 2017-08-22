# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from authentication.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            ## Lin,Leo - provide a context with error message to the user
            ## of why form validation failed!
            return render(request, 'authentication/signup.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            ## Lin,Leo - once the user has successfully signed-in, we
            ## redirect them to their own portal
            return redirect('home')  ## - TODO: redirect user to their own portal

    else:
        return render(request, 'authentication/signup.html',
                      {'form': SignUpForm()})
