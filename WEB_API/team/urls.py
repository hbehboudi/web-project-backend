from django.urls import path

from team.views import members_list, news_list, info, slider_images, team_statistics, league_list, game_list

urlpatterns = [
    path('<str:team_slug>/news/', news_list),
    path('<str:team_slug>/info/', info),
    path('<str:team_slug>/members/', members_list),
    path('<str:team_slug>/slider/', slider_images),
    path('<str:team_slug>/statistics/', team_statistics),
    path('<str:team_slug>/leagues/', league_list),
    path('<str:team_slug>/games/', game_list),
]
