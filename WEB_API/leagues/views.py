from django.db import OperationalError
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game, Goal
from leagues.models import League
from membership.models import TeamLeague
from news.models import News


@api_view()
def info(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        league_info = league.values('name', 'year', 'image_url', 'country', 'confederation', 'level', 'numberOfTeams',
                                     'bestTeam', 'establishedYear', 'website', 'field', 'active')
        return Response(league_info[0])
    except (IndexError, OperationalError):
        return Response({})


@api_view()
def newsList(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        tag_titles = league.tags.values_list('title')
        news = News.objects.filter(tags__title__in=tag_titles, deleted=False)
        return Response(news.values('title', 'category', 'image_url', 'created_date_time', 'slug'))
    except IndexError:
        return Response({})


@api_view()
def slider_images(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        sliders = league.objects.filter(league=league, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})


@api_view()
def league_list(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)

        result = league.values('name', 'year')[0]
        league = league[0]

        result['teams'] = TeamLeague.objects.filter(league=league).values('team__name')

        for team in result['teams']:
            team['game_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name']) | Q(team2__name=team['team__name'])).count()

            team['win_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name'], team_state1='W') |
                       Q(team2__name=team['team__name'], team_state2='W')).count()

            team['lose_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name'], team_state1='L') |
                       Q(team2__name=team['team__name'], team_state2='L')).count()

            team['draw_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name'], team_state1='D') |
                       Q(team2__name=team['team__name'], team_state2='D')).count()

            team['scoring_goal_number'] = Goal.objects.\
                filter(deleted=False, game__league=league, scoring_team__name=team['team__name']).count()

            team['receiving_goal_number'] = Goal.objects.\
                filter(deleted=False, game__league=league, receiving_team__name=team['team__name']).count()

            team['difference'] = team['scoring_goal_number'] - team['receiving_goal_number']

            team['score'] = team['win_number'] * 3 + team['draw_number']
        return Response(result)
    except IndexError:
        return Response({})


