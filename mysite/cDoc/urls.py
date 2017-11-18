from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^a/$', views.a, name='a'),
    url(r'^b/$', views.b, name='b'),
]