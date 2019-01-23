from rest_framework import serializers

from news.models import News, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'tag'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'summary', 'text', 'category', 'create_date_time',
                  'image_url', 'field', 'url']
