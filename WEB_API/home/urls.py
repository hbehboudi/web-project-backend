from django.urls import path

from home.views import football_news_list, basketball_news_list, slider_images, league_table, game_list, \
    league_game, league_names, like_football_news_list, like_basketball_news_list

urlpatterns = [
    path('news/all/football/', football_news_list),
    path('news/all/basketball/', basketball_news_list),
    path('news/like/football/', like_football_news_list),
    path('news/like/basketball/', like_basketball_news_list),
    path('slider-images/', slider_images),
    # path('league-tables/', league_tables),
    path('league-tables/<str:league_slug>/', league_table),
    path('games/', game_list),
    # path('league-games/', league_games),
    path('league-games/<str:league_slug>/', league_game),
    path('league-names/', league_names)
]
