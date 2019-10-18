from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^article/(?P<pk>\d+)$', views.details_page, name="article"),
    url(r'^about/$', views.about, name="about"),
    url(r'^search/$', views.search, name="search"),

    url(r'^project/$', views.project, name="projects"),
    url(r'^project/(?P<pk>\d+)/$', views.project_detail, name="project_detail"),
    url(r'^robots.txt$',
        TemplateView.as_view(template_name="website/robots.txt", content_type="text/plain"),
        name="robots_file"),
    url(r'^sitemap.xml$',
        TemplateView.as_view(template_name="website/sitemap.xml", content_type="text/plain"),
        name="sitemap_file"),
    url(r'^eve/$', views.eve, name="search"),

]

handler404 = 'website.views.handler404'
