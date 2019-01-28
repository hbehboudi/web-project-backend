from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from news.views import info

urlpatterns = [
    path('<str:news_slug>/', info),
]
