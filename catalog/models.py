# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
import uuid # Required for uniquely distinguish locations
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

import thumbs  #### this is not required, you can also delete thumbs.py
import uuid

class Category(models.Model):
    """
    Represents location category (e.g. Historic Towns, Ranch, etc ..)
    """
    name = models.CharField(max_length=200, help_text="Enter category for the location (e.g. Historic Towns, Ranch, Lakes, etc.")

    def __str__(self):
        """
        String that describes this model (in Admin site etc.)
        """
        return self.name

def image_upload_to(instance, filename):
   title = instance.title
   slug = slugify(title)
   basename, file_extension = filename.split(".")
   new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
   return "catalog/images/%s/%s" % (slug, new_filename)

class Location(models.Model):
    """
    Represents a location
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular location across whole catalog")

    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=70)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of this location")
    description = models.TextField(max_length=1024, help_text="Enter a detailed description for this location")

    created_user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    update_user = models.ForeignKey(User, null=True, blank=True, related_name="+")
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)

    views = models.IntegerField(null=True, blank=True, default=0)
    likes = models.IntegerField(null=True, blank=True, default=0)
    category = models.ManyToManyField('Category', help_text="Select a category for this location")

    thumb = ProcessedImageField(upload_to='catalog/images', processors=[ResizeToFit(300)], format='JPEG',
                                options={'quality': 90})


    #thumb = models.ImageField(upload_to=image_upload_to, default='catalog/images/icon.png')

    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        """
        metadata can be used to control the default ordering of records returned when you query the model type.
        if you prefix a minus symbol (-) it implies reverse the sorting order.  e.g. ordering = ['-update_date']
        """
        ordering = ['update_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular location
        """
        ### see url 'location-detail'
        return reverse('location-detail', kwargs={'pk': self.pk})

    def display_category(self):
        """
        Creates a string for the Category.  This is required to display category in Admin
        """
        return ', '.join([category.name for category in self.category.all()[:3]])
    display_category.short_description = 'Category'

class Image(models.Model):
    """
    Represents images from a location
    """
    image = ProcessedImageField(upload_to='catalog/images', processors=[ResizeToFit(1280)], format='JPEG',
                                options={'quality': 70})
    thumb = ProcessedImageField(upload_to='catalog/images', processors=[ResizeToFit(300)], format='JPEG',
                                options={'quality': 80})
    location = models.ForeignKey(Location, related_name='related_image')
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)