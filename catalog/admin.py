# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Location, Image


#superuser hayashi_leo
#password filmlocation1

admin.site.register(Location)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    list_filter = ('name', 'name')


admin.site.register(Image)