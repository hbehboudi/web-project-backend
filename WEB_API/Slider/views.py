from rest_framework import generics

from Slider.models import SliderImage
from Slider.serializers import SliderImageSerializer


class SliderImageList(generics.ListAPIView):
    images = SliderImage.objects.all().filter(deleted=False)
    serializer_class = SliderImageSerializer

    queryset = images
