from django.urls import path

from home.views import football_news_list, basketball_news_list, slider_images, league_tables, league_table, game_list, \
    league_games, league_game, league_names

urlpatterns = [
    path('news/football/', football_news_list),
    path('news/basketball/', basketball_news_list),
    path('slider-images/', slider_images),
    path('league-tables/', league_tables),
    path('league-tables/<str:league_slug>/', league_table),
    path('games/', game_list),
    path('league-games/', league_games),
    path('league-games/<str:league_slug>/', league_game),
    path('league-naems/', league_names)
]
