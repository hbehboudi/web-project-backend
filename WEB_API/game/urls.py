from django.urls import path


from . import views

urlpatterns = [
    path('<str:game_slug>/info/', views.info),
    path('<str:game_slug>/news/', views.newsList),
    path('<str:game_slug>/slider/', views.slider_images),
    path('<str:game_slug>/reports/', views.reportList),
]
