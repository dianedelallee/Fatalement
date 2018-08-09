
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^article/(?P<pk>\d+)$', views.details_page, name="article"),
    url(r'^about/$', views.about, name="about"),
]
