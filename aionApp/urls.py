from django.conf.urls import url
from .import views

app_name = 'aionApp'

urlpatterns= [
    url(r'^homePage/$', views.homePage, name='homePage'),
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
    url(r'^adminPage/$', views.adminPage, name='adminPage'),
    url(r'^homeLogIn/$', views.homeLogIn, name='homeLogIn'),
    url(r'^shopLogIn/$', views.shopLogIn, name='shopLogIn'),
    url(r'^exitSession/$', views.exitSession, name='exitSession'),
    url(r'^shopPage/$', views.shopPage, name='shopPage'),
    url(r'^addProduct/$', views.addProduct, name='addProduct'),
    url(r'^addToCart/$', views.addToCart, name='addToCart'),
    url(r'^signingUp/$', views.signingUp, name='signingUp'),
    url(r'^addAdmin/$', views.addAdmin, name='addAdmin'),
    url(r'^deleteProduct/(?P<id>[\w\-]+)$', views.deleteProduct, name='deleteProduct'),
    url(r'^editProduct/(?P<id>[\w\-]+)$', views.editProduct, name='editProduct'),
]