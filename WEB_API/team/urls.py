from django.urls import path

from team.views import members_list, info, slider_images, team_statistics, league_list, game_list, news_list_by_player,\
    news_list_by_team

urlpatterns = [
    path('<str:team_slug>/news/by-team/', news_list_by_team),
    path('<str:team_slug>/news/by-player/', news_list_by_player),
    path('<str:team_slug>/info/', info),
    path('<str:team_slug>/members/', members_list),
    path('<str:team_slug>/slider/', slider_images),
    path('<str:team_slug>/statistics/', team_statistics),
    path('<str:team_slug>/leagues/', league_list),
    path('<str:team_slug>/games/', game_list),
]
