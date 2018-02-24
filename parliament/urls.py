from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$', views.parliament, name='parliament'),
    url(r'^Committee/$', views.committee, name='committee'),
    url(r'^Elections/$', views.elections, name='elections'),
    url(r'^Minutes/$', views.minutes, name='minutes'),
    url(r'^Feedback/$', views.feedback, name='feedback'),
]