from django.conf.urls import url
from .import views

app_name = 'aionApp'

urlpatterns= [
    url(r'^homePage/$', views.homePage, name='homePage'),
    url(r'^registerPage/$', views.registerPage, name='registerPage'),
    url(r'^adminPage/$', views.adminPage, name='adminPage'),
    url(r'^accountingPage/$', views.accountingPage, name='accountingPage'),
    url(r'^homeLogIn/$', views.homeLogIn, name='homeLogIn'),
    url(r'^shopLogIn/$', views.shopLogIn, name='shopLogIn'),
    url(r'^exitSession/$', views.exitSession, name='exitSession'),
    url(r'^shopPage/$', views.shopPage, name='shopPage'),
    url(r'^addProduct/$', views.addProduct, name='addProduct'),
    url(r'^signingUp/$', views.signingUp, name='signingUp'),
    url(r'^addAdmin/$', views.addAdmin, name='addAdmin'),
    url(r'^deleteProduct/(?P<id>[\w\-]+)$', views.deleteProduct, name='deleteProduct'),
    url(r'^editProduct/(?P<id>[\w\-]+)$', views.editProduct, name='editProduct'),
    url(r'^buyProduct/(?P<id>[\w\-]+)$', views.buyProduct, name='buyProduct'),
    url(r'^checkOutProduct/$', views.checkOutProduct, name='checkOutProduct'),
    url(r'^profilePage/$', views.profilePage, name='profilePage'),
    url(r'^checkoutPage/$', views.checkoutPage, name='checkoutPage'),
    url(r'^purchasePage/$', views.purchasePage, name='purchasePage'),
    url(r'^addReview/(?P<id>[\w\-]+)$', views.addReview, name='addReview'),
    url(r'^reviewPage/(?P<id>[\w\-]+)$', views.reviewPage, name='reviewPage'),
    url(r'^editProfilePage/$', views.editProfilePage, name='editProfilePage'),
    url(r'^editingProfile/$', views.editingProfile, name='editingProfile'),
    url(r'^search/$', views.search, name='search'),
    url(r'^analog/$', views.analog, name='analog'),
    url(r'^digital/$', views.digital, name='digital'),
    url(r'^smart/$', views.smart, name='smart'),
]