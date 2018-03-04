from django.conf.urls import url
from .import views

app_name = 'aionApp'

urlpatterns= [
    url(r'^homePage/$', views.homePage, name='homePage'),
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
    url(r'^homeLogIn/$', views.homeLogIn, name='homeLogIn'),
    url(r'^shopLogIn/$', views.shopLogIn, name='shopLogIn'),
    url(r'^exitSession/$', views.exitSession, name='exitSession'),
    url(r'^shopPage/$', views.shopPage, name='shopPage'),
]