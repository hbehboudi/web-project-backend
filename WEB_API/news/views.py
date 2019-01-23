from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from news.models import News
from news.serializers import NewsSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
