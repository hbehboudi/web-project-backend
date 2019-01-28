from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News


@api_view()
def info(request, news_slug):
    try:
        news = News.objects.filter(slug__contains=news_slug, deleted=False)
        result = news.values('title', 'summary', 'text', 'category', 'image_url', 'field',
                             'created_date_time', 'slug')[0]
        result['tags'] = news[0].tags.values_list('title')
        result['related_news'] = News.objects.filter(tags__title__in=result['tags'], deleted=False)\
            .values('title', 'category', 'image_url', 'slug')

        return Response(result)
    except IndexError:
        return Response({})
