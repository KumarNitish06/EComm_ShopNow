from django.conf.urls import url,include
from . import views

urlpatterns = [

    url(r'^home/$',views.index, name='index'),
    url(r'^loggedin/$',views.index2, name='index2'),
    url(r'^details/',views.detail, name='detail'),
    url(r'^mobile/$',views.mobile, name='mobile'),
    url(r'^laptops/$',views.laptops, name='laptops'),
    url(r'^sports/$',views.sports, name='sports'),
    url(r'^fashion/$',views.fashion, name='fashion'),
    url(r'^electronics/$',views.electronics, name='electronics'),
    url(r'^search/$',views.search, name="search"),
    url(r'^buynow/',views.buynow, name="search"),
    url(r'^',include('Userform.urls')),
    url(r'^',include('cart.urls')),
  
]
