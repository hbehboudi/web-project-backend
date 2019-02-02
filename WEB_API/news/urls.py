from django.urls import path

from news.views import info, comment_list, create_comment

urlpatterns = [
    path('<str:news_slug>/', info),
    path('', create_comment),
    path('<str:news_slug>/comment/', comment_list),
]
