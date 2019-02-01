from django.db import OperationalError
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

from game.models import Game
from home.models import SliderImage
from leagues.models import League
from membership.models import TeamLeague
from news.models import News
from django.utils import timezone


@api_view()
def football_news_list(request):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        football_news = News.objects.all().filter(deleted=False, field='FTB')[0: int(num)].\
            values('title', 'summary', 'text', 'type__title', 'image_url', 'field', 'slug', 'created_date_time')
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
            values('title', 'summary', 'text', 'type__title', 'image_url', 'field', 'slug', 'created_date_time')
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


# @api_view()
# def league_tables(request):
#     try:
#         leagues = League.objects.all().values('name', 'year', 'field', 'slug')
#         for league in leagues:
#             league['teams'] = TeamLeague.objects. \
#                 filter(league__name=league['name'], league__year=league['year']).values('team__name', 'team__slug')
#             for team in league['teams']:
#                 team['game_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
#                                                           league__year=league['year']). \
#                     filter(Q(team1__name=team['team__name']) | Q(team2__name=team['team__name'])).count()
#
#                 team['win_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
#                                                          league__year=league['year']). \
#                     filter(Q(team1__name=team['team__name'], team_state1='W') |
#                            Q(team2__name=team['team__name'], team_state2='W')).count()
#
#                 team['lose_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
#                                                           league__year=league['year']). \
#                     filter(Q(team1__name=team['team__name'], team_state1='L') |
#                            Q(team2__name=team['team__name'], team_state2='L')).count()
#
#                 if league['field'] == 'FTB':
#                     team['draw_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
#                                                               league__year=league['year']). \
#                         filter(Q(team1__name=team['team__name'], team_state1='D') |
#                                Q(team2__name=team['team__name'], team_state2='D')).count()
#
#                     team['score'] = team['win_number'] * 3 + team['draw_number']
#         return Response(leagues)
#     except IndexError:
#         return Response({})


@api_view()
def league_table(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False).values('name', 'year', 'field')[0]
        league['teams'] = TeamLeague.objects.filter(league__name=league['name'], league__year=league['year']).\
            values('team__name', 'team__slug')
        for team in league['teams']:
            team['game_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
                                                      league__year=league['year']). \
                filter(Q(team1__name=team['team__name']) | Q(team2__name=team['team__name'])).count()

            team['win_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
                                                     league__year=league['year']). \
                filter(Q(team1__name=team['team__name'], team_state1='W') |
                       Q(team2__name=team['team__name'], team_state2='W')).count()

            team['lose_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
                                                      league__year=league['year']). \
                filter(Q(team1__name=team['team__name'], team_state1='L') |
                       Q(team2__name=team['team__name'], team_state2='L')).count()

            if league['field'] == 'FTB':
                team['draw_number'] = Game.objects.filter(deleted=False, league__name=league['name'],
                                                          league__year=league['year']). \
                    filter(Q(team1__name=team['team__name'], team_state1='D') |
                           Q(team2__name=team['team__name'], team_state2='D')).count()

                team['score'] = team['win_number'] * 3 + team['draw_number']

        if league['field'] == 'FTB':
            league['teams'] = sorted(league['teams'], key=lambda i: i['score'], reverse=True)
        else:
            league['teams'] = sorted(league['teams'], key=lambda i: i['win_number'], reverse=True)
        counter = 0
        for team in league['teams']:
            counter += 1
            team['rank'] = counter

        return Response(league)
    except IndexError:
        return Response({})


@api_view()
def game_list(request):
    try:
        football_games = Game.objects.filter(game_date__gte=timezone.now() - datetime.timedelta(days=1), field='FTB',
                                             game_date__lte=timezone.now() + datetime.timedelta(days=1), deleted=False)\
            .values('team1__name', 'team2__name', 'team1__image_url', 'team2__image_url', 'goals1', 'goals2',
                    'full_time', 'game_date', 'league__name', 'league__year', 'field', 'team_state1', 'team_state2')
        basketball_games = Game.objects.filter(game_date__gte=timezone.now() - datetime.timedelta(days=1),
                                               game_date__lte=timezone.now() + datetime.timedelta(days=1),
                                               field='BSK', deleted=False).\
            values('team1__name', 'team2__name', 'team1__image_url', 'team2__image_url', 'all_score1', 'all_score2',
                   'full_time', 'game_date', 'league__name', 'league__year', 'field', 'team_state1', 'team_state2')
        result = []
        for game in football_games:
            result.append(game)
        for game in basketball_games:
            result.append(game)
        return Response(result)
    except IndexError:
        return Response({})


# @api_view()
# def league_games(request):
#     try:
#         leagues = League.objects.all().filter(deleted=False).values('name', 'year')
#         for league in leagues:
#             league['games'] = Game.objects.filter(deleted=False, league__name=league['name'],
#                                                   league__year=league['year']).values('team1__name', 'team2__name',
#                                                                                       'team1__image_url',
#                                                                                       'team2__image_url',
#                                                                                       'goals1', 'goals2', 'full_time',
#                                                                                       'game_date', 'slug')
#         return Response(leagues)
#     except IndexError:
#         return Response({})


@api_view()
def league_game(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False).values('name', 'year', 'field')[0]
        if league['field'] == "FTB":
            league['games'] = Game.objects.filter(deleted=False, league__name=league['name'],
                                                  league__year=league['year']).\
                values('team1__name', 'team2__name', 'team1__image_url', 'team2__image_url', 'goals1', 'goals2',
                       'full_time', 'game_date', 'slug', 'field')
        else:
            league['games'] = Game.objects.filter(deleted=False, league__name=league['name'],
                                                  league__year=league['year']). \
                values('team1__name', 'team2__name', 'team1__image_url', 'team2__image_url', 'all_score1', 'all_score2',
                       'full_time', 'game_date', 'slug', 'field')
        return Response(league)
    except IndexError:
        return Response({})


@api_view()
def league_names(request):
    try:
        leagues = {
            'football': [],
            'basketball': [],
        }

        for league in League.objects.filter(deleted=False, field='FTB', active=True).values('name', 'slug'):
            leagues['football'].append({
                'key': league['slug'],
                'value': league['slug'],
                'text': league['name'],
            })
        for league in League.objects.filter(deleted=False, field='BSK', active=True).values('name', 'slug'):
            leagues['basketball'].append({
                'key': league['slug'],
                'value': league['slug'],
                'text': league['name'],
            })
        return Response(leagues)
    except IndexError:
        return Response({})
