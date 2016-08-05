from django.conf.urls import url
from . impor views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
