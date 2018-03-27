from django.conf.urls import url, include
from . import views
urlpatterns = [

    url(r'^$', views.loggedin),
    url(r'^courses/creating$', views.creating),
    url(r'^courses$', views.courses),
    url(r'^add$', views.add),
    url(r'^(?P<course_id>\d+)/view$', views.view),
    url(r'^(?P<course_id>\d+)/update$', views.update),
    url(r'^(?P<course_id>\d+)/updating$', views.updating),
    url(r'^(?P<course_id>\d+)/like$', views.like),
    url(r'^(?P<course_id>\d+)/unlike$', views.unlike),
    url(r'^(?P<course_id>\d+)/delete$', views.delete),
]