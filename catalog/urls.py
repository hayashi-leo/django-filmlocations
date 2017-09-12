
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from catalog import views as catalog_views

urlpatterns = [
    url(r'^$', catalog_views.listing, name='catalog_listing'),
    ### [-\w] regex: create a 'character class', match '-' or any word char
    url(r'^(?P<slug>[-\w]+)$', catalog_views.LocationDetail.as_view(), name='location'),
    url(r'^(?P<slug>[-\w]+)/update/$', catalog_views.LocationUpdate.as_view(), name='location_update_slug')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

