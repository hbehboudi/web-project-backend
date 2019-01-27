from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(r'', views.TeamViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('<str:team_slug>/members/', views.members_list),
    path('<str:team_slug>/news/', views.news_list),
    path('<str:team_slug>/info/', views.info),
    path('<str:team_slug>/slider/', views.slider_images),
]
