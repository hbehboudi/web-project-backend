from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game
from membership.models import PlayerTeam
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
        player_info = Player.objects.values('name', 'image_url', 'post__name', 'field', 'age', 'city', 'height',
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


# @api_view()
# def player_statistics(request, player_slug):
#     try:
#         player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
#         leagues = PlayerTeam.objects.filter(player=player, deleted=False).values('teamLeague__league__name',
#                                                                                  'teamLeague__league__year')
#
#         for league in leagues:
#             player_team = PlayerTeam.objects.filter(player=player, deleted=False,
#                                                     teamLeague__league__name=league['teamLeague__league__name'],
#                                                     teamLeague__league__year=league['teamLeague__league__year'])[0]
#
#             league['team'] = player_team.teamLeague.team.name
#             league['num'] = player_team.num
#             league['games'] = Game.objects.filter(league__name=league['teamLeague__league__name'],
#                                                   league__year=league['teamLeague__league__year'],
#                                                   deleted=False, =)
#
#             league['scoring_goal_number'] = Goal.objects.\
#                 filter(game__league__name=league['league__name'], deleted=False, scoring_team=team).count()
#
#             league['receiving_goal_number'] = Goal.objects.\
#                 filter(game__league__name=league['league__name'], deleted=False, receiving_team=team).count()
#
#             league['win_num'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
#                 filter(Q(team1=team, team_state1='W') | Q(team2=team, team_state2='W')).count()
#
#             league['lose_num'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
#                 filter(Q(team1=team, team_state1='L') | Q(team2=team, team_state2='L')).count()
#
#             league['draw_num'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
#                 filter(Q(team1=team, team_state1='D') | Q(team2=team, team_state2='D')).count()
#
#         return Response(leagues)
#     except IndexError:
#         return Response({})
