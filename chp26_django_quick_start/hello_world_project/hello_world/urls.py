from django.conf.urls import url
from hello_world import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^better/$', views.better, name='better'),
    url(r'^$', views.index, name='index'),
]