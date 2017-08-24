# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


"""
If you're using function-based views, the easiest way to restrict access to your
functions is to apply the @login_required to your view function.  If the user is 
logged-in, then your view code will execute as normal.  If the user is not logged-in,
this will redirect to the login url defined in the project settings 'LOGIN_URL=',
passing the current absolute path as the 'next' URL parameter.
"""

from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return render(request, 'home.html')

