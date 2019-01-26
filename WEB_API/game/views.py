from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game, GameSliderImage, GameReport
from news.models import News


@api_view()
def info(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)
        game_state = game.values('team1__name', 'team2__name', 'team1__slug', 'team2__slug', 'team1__image_url',
                                 'team2__image_url', 'shots1', 'shots2', 'shots_on_target1', 'shots_on_target2',
                                 'possession1', 'possession2', 'passes1', 'passes2', 'fouls1', 'fouls2',
                                 'yellow_cards1', 'yellow_cards2', 'red_cards1', 'red_cards2', 'offsides1',
                                 'offsides2', 'corners1', 'corners2')
        return Response(game_state[0])
    except (IndexError, OperationalError):
        return Response({})


@api_view()
def newsList(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        tag_titles = game.tags.values_list('title')
        news = News.objects.filter(tags__title__in=tag_titles, deleted=False)
        return Response(news.values('title', 'category', 'image_url', 'created_date_time', 'slug'))
    except IndexError:
        return Response({})


@api_view()
def slider_images(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        sliders = GameSliderImage.objects.filter(game=game, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})


@api_view()
def reportList(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        reports = GameReport.objects.filter(game=game, deleted=False).values('title', 'image_url', 'minute', 'second')
        return Response(reports)
    except IndexError:
        return Response({})
