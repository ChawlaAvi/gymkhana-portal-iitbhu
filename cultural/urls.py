from django.conf.urls import url
from . import views



urlpatterns = [
	
	url(r'^$', views.cultural, name='cultural'),
    url(r'^clubs/fac$', views.fac, name='fac'),
	url(r'^clubs/imc$', views.imc, name='imc'),
	url(r'^clubs/wmc$', views.wmc, name='wmc'),
	url(r'^clubs/lit$', views.lit, name='lit'),
	url(r'^clubs/dance$', views.dance, name='dance'),
	url(r'^clubs/quiz$', views.quiz, name='quiz'),
	url(r'^clubs/theatre$', views.theatre, name='theatre'),
]