from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^registration$', views.registration, name="registration"),
    url(r'^login$', views.login, name="login"),
    url(r'^loggedin$', views.loggedin, name="loggedin"),
    url(r'^logout$', views.logout, name="logout"),
]