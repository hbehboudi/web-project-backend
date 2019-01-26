from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News
from player.models import Player, PlayerSliderImage


@api_view()
def newsList(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        tag_titles = player.tags.values_list('title')
        news = News.objects.filter(tags__title__in=tag_titles, deleted=False)
        return Response(news.values('title', 'category', 'image_url', 'field', 'created_date_time', 'slug'))
    except IndexError:
        return Response({})


@api_view()
def info(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)
        player_info = player.values('name', 'image_url', 'post', 'field', 'age', 'city', 'height', 'weight', 'teamNum',
                                    'nationalityTeamNum', 'website')
        return Response(player_info[0])
    except (IndexError, OperationalError):
        return Response({})


@api_view()
def slider_images(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        sliders = PlayerSliderImage.objects.filter(player=player, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})

