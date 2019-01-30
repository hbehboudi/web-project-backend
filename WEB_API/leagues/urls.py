from django.urls import path


from . import views

urlpatterns = [
    path('<str:league_slug>/info/', views.info),
    path('<str:league_slug>/news/', views.newsList),
    path('<str:league_slug>/slider/', views.slider_images),
    path('<str:league_slug>/statistics/', views.league_list),
    path('<str:league_slug>/best_players/', views.best_player_list),
    path('<str:league_slug>/games/', views.game_list),
]
