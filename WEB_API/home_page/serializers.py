from rest_framework import serializers

from home_page.models import SliderImage


class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ['title', 'image_url']
