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
    path('<str:teamSlug>/members/', views.memberList),
    path('<str:teamSlug>/news/', views.newsList),
]
