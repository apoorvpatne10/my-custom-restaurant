from django.conf.urls import url
from django.contrib import admin
from restaurants import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', views.RestaurantListView.as_view(), name='list'),
    url(r'^create/$', views.RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.RestaurantUpdateView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', views.RestaurantUpdateView.as_view(), name='edit'),
]
