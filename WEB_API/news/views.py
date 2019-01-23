from rest_framework import generics

from news.models import News
from news.serializers import NewsSerializer


class FootballNewsList(generics.ListAPIView):
    football = News.objects.all().filter(deleted=False, field='FTB')[0: 50]
    serializer_class = NewsSerializer

    queryset = football


class BasketballNewsList(generics.ListAPIView):
    basketball = News.objects.all().filter(deleted=False, field='BSK')[0: 50]
    serializer_class = NewsSerializer

    queryset = basketball

