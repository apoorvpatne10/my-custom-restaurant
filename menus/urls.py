from django.conf.urls import url
from django.contrib import admin
from menus import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    # url(r'^(?P<pk>\d+)/edit/$', views.ItemUpdateView.as_view(), name='edit'),
    url(r'^$', views.ItemListView.as_view(), name='list'),
    url(r'^create/$', views.ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ItemUpdateView.as_view(), name='detail'),
]
