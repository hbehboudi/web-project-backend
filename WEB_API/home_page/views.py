from rest_framework import generics

from home_page.models import SliderImage
from home_page.serializers import SliderImageSerializer


class SliderImageList(generics.ListAPIView):
    images = SliderImage.objects.all().filter(deleted=False)
    serializer_class = SliderImageSerializer

    queryset = images
