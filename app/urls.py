from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name="index"),
    url(r'^column/$', views.column, name="column"),
    url(r'^contact/$', views.contact, name="contact"),
]
