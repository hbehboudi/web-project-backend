from rest_framework import serializers

from Slider.models import SliderImage


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ['title', 'image_url']
