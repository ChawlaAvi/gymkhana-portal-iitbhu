from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^parliament/', include('parliament.urls')),
    url(r'', include('home.urls')),
	url(r'^fmc/', include('fmc.urls')),
	url(r'^sntc/', include('sntc.urls')),
	url(r'^gnsc/', include('gnsc.urls')),
	url(r'^cultural/', include('cultural.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)