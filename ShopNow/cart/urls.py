from django.conf.urls import url,include
from . import views

urlpatterns = [

    
    url(r'^add/(?P<id>\d+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(?P<id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/$', views.view, name='cart'),
    
]
