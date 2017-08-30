"""properties URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from newsletter import views as newsletter_views
from authentication import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', newsletter_views.home, name='home'),
    url(r'^signup/$', auth_views.signup, name='signup'),

    url(r'^catalog/', include('catalog.urls')),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [url(r'^accounts/', include('django.contrib.auth.urls')),]

"""
Serving static files in development
Make sure the 'django.contrib.staticfiles' app is added in our INSTALLED_APP under settings.
"""

"""
Serving media files in development
"""

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


