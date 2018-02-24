from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.fmc, name='fmc'),
    url(r'^clubs/animation$', views.animation, name='animation'),
	url(r'^clubs/cine$', views.cine, name='cine'),
	url(r'^clubs/design$', views.design, name='design'),
	url(r'^clubs/media$', views.media, name='media'),
	url(r'^clubs/outreach$', views.outreach, name='outreach'),
	url(r'^clubs/photography$', views.photography, name='photography'),
]