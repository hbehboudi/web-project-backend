from django.urls import path

from home_page.views import SliderImageList

urlpatterns = [
    path('slider-images/', SliderImageList.as_view()),
]
