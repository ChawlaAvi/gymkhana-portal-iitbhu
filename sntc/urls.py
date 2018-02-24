from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^clubs/aero_modelling$', views.amc, name='amc'),
    url(r'^clubs/astronomy$', views.astro, name='astro'),
    url(r'^clubs/cops$', views.cops, name='cops'),
    url(r'^clubs/green$', views.green, name='green'),
    url(r'^clubs/troc$', views.troc, name='troc'),
    url(r'^clubs/robotics$', views.robotics, name='robotics'),
    url(r'^clubs/sae$', views.sae, name='sae'),
    url(r'^clubs/cef$', views.cef, name='cef'),
    url(r'^teams/trident$', views.trident, name='trident'),
    url(r'^teams/vocowa$', views.vocowa, name='vocowa'),
    url(r'^teams/auv$', views.auv, name='auv'),
    url(r'^app/$', views.app, name='app'),
]
