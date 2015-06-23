from django.conf.urls import include, url
from todo import views

urlpatterns = [
    url(r'^$', views.home),
]
