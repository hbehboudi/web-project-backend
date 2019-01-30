from django.urls import path


from . import views

urlpatterns = [
    path('<str:league_slug>/info/', views.info),
    path('<str:league_slug>/news/', views.newsList),
    path('<str:league_slug>/slider/', views.slider_images),
    path('<str:league_slug>/statistics/', views.league_list),

]
