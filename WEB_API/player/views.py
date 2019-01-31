from django.db import OperationalError
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game, Substitute, Goal
from membership.models import PlayerTeam, PlayerGame
from news.models import News
from player.models import Player, PlayerSliderImage


@api_view()
def news_list(request, player_slug):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        news = News.objects.filter(Q(title__contains=player.name) | Q(tags__title__contains=player.name) |
                                   Q(text__contains=player.name) | Q(summary__contains=player.name))
        return Response(news.values('title', 'category', 'image_url', 'field',
                                    'created_date_time', 'slug')[0: int(num)])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def info(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)
        player_info = player.values('name', 'image_url', 'post__name', 'field', 'age', 'city', 'height',
                                            'weight', 'teamNum', 'nationalityTeamNum', 'website')
        return Response(player_info[0])
    except (IndexError, AssertionError, OperationalError):
        return Response({'error': True})


@api_view()
def slider_images(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        sliders = PlayerSliderImage.objects.filter(player=player, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})


@api_view()
def player_statistics(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        leagues = PlayerTeam.objects.filter(player=player, deleted=False).values('teamLeague__league__name',
                                                                                 'teamLeague__league__year')

        for league in leagues:
            player_team = PlayerTeam.objects.filter(player=player, deleted=False,
                                                    teamLeague__league__name=league['teamLeague__league__name'],
                                                    teamLeague__league__year=league['teamLeague__league__year'])

            league['team'] = player_team[0].teamLeague.team.name

            league['num'] = player_team[0].num

            league['game_num'] = PlayerGame.objects.\
                                     filter(player=player, team__name=league['team'], deleted=False,
                                            game__league__name=league['teamLeague__league__name'],
                                            game__league__year=league['teamLeague__league__year']).count() + \
                                 Substitute.objects.\
                                     filter(in_player=player, team__name=league['team'], deleted=False,
                                            game__league__name=league['teamLeague__league__name'],
                                            game__league__year=league['teamLeague__league__year']).count()

            league['scoring_goal_number'] = Goal.objects. \
                filter(player=player, deleted=False, scoring_team__name=league['team'], penalty=False, own_goal=False,
                       game__league__name=league['teamLeague__league__name'],
                       game__league__year=league['teamLeague__league__year']).count()

            league['scoring_penalty_goal_number'] = Goal.objects. \
                filter(player=player, deleted=False, scoring_team__name=league['team'], penalty=True, own_goal=False,
                       game__league__name=league['teamLeague__league__name'],
                       game__league__year=league['teamLeague__league__year']).count()

        return Response(leagues)
    except IndexError:
        return Response({})
