from django.conf.urls import url
from .import views

app_name = 'aionApp'

urlpatterns= [
    url(r'^homePage/$', views.homePage, name='homePage'),
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
]