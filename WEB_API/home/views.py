from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import SliderImage
from news.models import News


@api_view()
def football_news_list(request):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        football_news = News.objects.all().filter(deleted=False, field='FTB')[0: int(num)].\
            values('title', 'summary', 'text', 'category', 'image_url', 'field', 'slug', 'created_date_time')
        return Response(football_news)
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def basketball_news_list(request):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        basketball_news = News.objects.all().filter(deleted=False, field='BSK')[0: int(num)].\
            values('title', 'summary', 'text', 'category', 'image_url', 'field', 'slug', 'created_date_time')
        return Response(basketball_news)
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def slider_images(request):
    try:
        num = request.GET.get('n')
        slider = SliderImage.objects.all().filter(deleted=False).values('title', 'image_url')
        if num:
            slider = slider[0: int(num)]
        return Response(slider)
    except (IndexError, AssertionError, OperationalError):
        return Response({})
