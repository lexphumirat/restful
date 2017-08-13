from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^checkusers$', views.checkusers),
    url(r'^create_user$', views.create_user),
    url(r'^showuser$', views.showuser),
    url(r'^user/(?P<id>\d+)$' , views.showuser)

        # This line has changed!
  ]
