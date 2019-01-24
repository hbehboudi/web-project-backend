from django.urls import path

from Slider.views import SliderImageList

urlpatterns = [
    path('slider-images/', SliderImageList.as_view()),
]
