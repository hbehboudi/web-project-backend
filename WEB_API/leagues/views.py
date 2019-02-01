from django.db import OperationalError
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game, Goal, Throw, Ribbond, Foul
from leagues.models import League, BestPlayer, LeagueSliderImage
from membership.models import TeamLeague
from news.models import News


@api_view()
def info(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)
        league_info = league.values('name', 'year', 'image_url', 'country', 'confederation', 'level', 'numberOfTeams',
                                     'bestTeam', 'establishedYear', 'website', 'field', 'active')
        return Response(league_info[0])
    except (IndexError, OperationalError):
        return Response({})


@api_view()
def newsList(request, league_slug):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        news = News.objects.filter(Q(title__contains=league.name) | Q(tags__title__contains=league.name) |
                                   Q(text__contains=league.name) | Q(summary__contains=league.name))

        return Response(news.values('title', 'type__title', 'image_url', 'field',
                                    'created_date_time', 'slug')[0: int(num)])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def slider_images(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        sliders = LeagueSliderImage.objects.filter(league=league, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})


@api_view()
def league_list(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)

        result = league.values('name', 'year', 'field')[0]
        league = league[0]

        result['teams'] = TeamLeague.objects.filter(league=league).values('team__name', 'team__field', 'team__slug')

        for team in result['teams']:
            team['game_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name']) | Q(team2__name=team['team__name'])).count()

            team['win_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name'], team_state1='W') |
                       Q(team2__name=team['team__name'], team_state2='W')).count()

            team['lose_number'] = Game.objects.filter(deleted=False, league=league).\
                filter(Q(team1__name=team['team__name'], team_state1='L') |
                       Q(team2__name=team['team__name'], team_state2='L')).count()
            if team['team__field'] == "FTB":
                team['draw_number'] = Game.objects.filter(deleted=False, league=league).\
                    filter(Q(team1__name=team['team__name'], team_state1='D') |
                           Q(team2__name=team['team__name'], team_state2='D')).count()

                team['scoring_goal_number'] = Goal.objects.\
                    filter(deleted=False, game__league=league, scoring_team__name=team['team__name']).count()

                team['receiving_goal_number'] = Goal.objects.\
                    filter(deleted=False, game__league=league, receiving_team__name=team['team__name']).count()

                team['difference'] = team['scoring_goal_number'] - team['receiving_goal_number']

                team['score'] = team['win_number'] * 3 + team['draw_number']
            else:
                team['score3_number'] = Throw.objects.\
                    filter(deleted=False, score="3", game__league=league, team__name=team['team__name']).count()
                team['ribbond_number'] = Ribbond.objects.\
                    filter(deleted=False, game__league=league, team__name=team['team__name']).count()
                team['foul_number'] = Foul.objects.\
                    filter(deleted=False, game__league=league, team__name=team['team__name']).count()
        if result['field'] == 'FTB':
            result['teams'] = sorted(result['teams'], key=lambda i: i['difference'], reverse=True)
            result['teams'] = sorted(result['teams'], key=lambda i: i['score'], reverse=True)
        else:
            result['teams'] = sorted(result['teams'], key=lambda i: i['win_number'], reverse=True)
        counter = 0
        for team in result['teams']:
                counter += 1
                team['rank'] = counter
        return Response(result)
    except IndexError:
        return Response({"error": 404})


@api_view()
def best_player_list(request, league_slug):
    try:
        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        best_players = BestPlayer.objects.filter(league=league, deleted=False, ).values('player__name', 'title',
                                                                                        'player__post__name',
                                                                                        'player__slug',
                                                                                        'player__image_url')
        return Response(best_players)
    except IndexError:
        return Response({"error": 404})


@api_view()
def game_list(request, league_slug):
    try:
        level = request.GET.get('level')

        league = League.objects.filter(slug__contains=league_slug, deleted=False)[0]
        games = Game.objects.filter(league=league, deleted=False)

        if level:
            games = games.filter(level=level)
        if league.field == "FTB":
            games = games.values('team1__name', 'team2__name', 'team1__slug', 'team2__slug', 'slug',
                                 'team1__image_url', 'team2__image_url', 'goals1', 'goals2')
        else:
            games = games.values('team1__name', 'team2__name', 'team1__slug', 'team2__slug', 'slug',
                                 'team1__image_url', 'team2__image_url', 'all_score1', 'all_score2')
        return Response(games)
    except IndexError:
        return Response({"error": 404})
