# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from catalog.models import Category, Location


def home(request):
    categories = Category.objects.all()[:5]
    locations = Location.objects.all()

    return render(request, 'home.html', {'locations' : locations })

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

