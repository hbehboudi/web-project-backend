from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from news.views import FootballNewsList, BasketballNewsList

urlpatterns = [
    path('football/', FootballNewsList.as_view()),
    path('basketball/', BasketballNewsList.as_view()),
]
