from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from news import views

urlpatterns = [
    path('', views.NewsList.as_view()),
]
