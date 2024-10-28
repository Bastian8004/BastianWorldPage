from django.urls import path
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import BW.forms
import BW.views

from django.urls import include, re_path
from django.views.static import serve
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', include('BW.urls')),
    # Auth related urls
    path('accounts/', include('allauth.urls')),
     # Uncomment the next line to enable the admin:
    path('nimda/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('captcha/', include('captcha.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]

handler404 = 'BW.views.error_404_view'

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)