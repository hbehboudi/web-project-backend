from django.urls import path

from player.views import info, player_statistics, slider_images, news_list, like_check, liking

urlpatterns = [
    path('<str:player_slug>/info/', info),
    path('<str:player_slug>/slider/', slider_images),
    path('<str:player_slug>/statistics/', player_statistics),
    path('<str:player_slug>/news/', news_list),
    path('<str:player_slug>/like/', liking),
    path('<str:player_slug>/like_check/', like_check),
]
