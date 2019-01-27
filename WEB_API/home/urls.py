from django.urls import path

from home.views import football_news_list, basketball_news_list, slider_images

urlpatterns = [
    path('news/football/', football_news_list),
    path('news/basketball/', basketball_news_list),
    path('slider-images/', slider_images),
]
