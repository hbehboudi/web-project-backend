from django.urls import path

from player.views import info

urlpatterns = [
    path('<str:player_slug>/info/', info),
]
