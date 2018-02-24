from django.conf.urls import include, url
from . import views



urlpatterns = [
	
	url(r'^$', views.home, name='home'),
    url(r'^Gallery/$', views.gallery, name='gallery'),
    url(r'^Contact_us/$', views.contact, name='contact'),
	url(r'^credits/$', views.credits, name='credits'),
]