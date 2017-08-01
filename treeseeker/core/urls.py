from django.conf.urls import url, include
from django.contrib import admin
from .views import TreeSpeciesList

urlpatterns = [
    url(r'^$', TreeSpeciesList.as_view(), name='species-list'),
]
