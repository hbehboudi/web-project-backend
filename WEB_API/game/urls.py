from django.urls import path


from . import views

urlpatterns = [
    path('<str:game_slug>/info/', views.info),
    path('<str:game_slug>/players/', views.player_list),
    path('<str:game_slug>/time_lines/', views.time_lines),
    path('<str:game_slug>/news/', views.newsList),
    path('<str:game_slug>/reports/', views.reportList),
    path('<str:game_slug>/slider/', views.slider_images),
]
