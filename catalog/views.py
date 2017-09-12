# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from .models import Location, Image


### django generic editing views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


def listing(request):
    list = Location.objects.filter(is_visible=True).order_by('-created_date')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        locations = paginator.page(page)   ### where is 'albums' used for?
    except PageNotAnInteger:
        locations = paginator.page(1) # If page is not an integer, deliver first page
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)
    return render(request, 'listing.html', {'featured_locations' : locations, 'locations' : locations})

class LocationDetail(DetailView):
    model = Location
    template_name = 'catalog/listing_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LocationDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all hte images
        context['images'] = Image.objects.filter(location=self.object.id)
        return context

## see mozilla django-locallibrary tutorial
class LocationUpdate(UpdateView):
    model = Location
    template_name = 'catalog/listing_update.html'
    fields = '__all__' ## include all fields
    ## fields = ['summary', 'description'] ## include only these fields

    def get_success_url(self):
        return reverse('location', kwargs={'slug': self.kwargs['slug']})
