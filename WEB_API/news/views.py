from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from news.models import News, Comment


@api_view()
def info(request, news_slug):
    try:
        news = News.objects.filter(slug__contains=news_slug, deleted=False)
        result = news.values('title', 'summary', 'text', 'type__title', 'image_url', 'field',
                             'created_date_time', 'slug')[0]
        result['tags'] = news[0].tags.values_list('title')[0]
        result['related_news'] = News.objects.filter(tags__title__in=result['tags'], deleted=False)\
            .values('title', 'type__title', 'image_url', 'slug')

        return Response(result)
    except IndexError:
        return Response({})


@api_view(['POST'])
def create_comment(request):
    try:
        news = News.objects.filter(deleted=False, slug__contains=request.data['slug'])[0]
        user = Token.objects.filter(key__contains=request.data['token'])[0].user
        # user = Token.objects.get(key=request.data['token'])[0].user
        if request.method == 'POST':
            comment = Comment(title=request.data['title'], text=request.data['text'],
                              news=news, created_date_time=timezone.now(), user=user)
            comment.save()
        return Response({"comment": "create"})
    except IndexError:
        return Response({"comment": "error"})


@api_view()
def comment_list(request, news_slug):
    try:
        news = News.objects.filter(deleted=False, slug__contains=news_slug)[0]
        comments = Comment.objects.filter(news=news, deleted=False).values('title', 'text', 'created_date_time',
                                                                           'user__username').\
            order_by('created_date_time')
        return Response(comments)
    except IndexError:
        return Response({})
