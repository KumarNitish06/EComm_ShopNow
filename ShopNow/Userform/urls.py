from django.conf.urls import url,include
from . import views

urlpatterns = [

    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^login/$', views.login, name='login'),
    
]
