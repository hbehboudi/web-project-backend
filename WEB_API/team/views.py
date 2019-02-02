from django.db import OperationalError
from django.db.models import Q
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from game.models import Game, Goal
from news.models import News
from team.models import Team, TeamSliderImage, LikeTeam
from membership.models import PlayerTeam, TeamLeague


@api_view()
def news_list_by_team(request, team_slug):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        news = News.objects.filter(Q(title__contains=team.name) | Q(tags__title__contains=team.name) |
                                   Q(text__contains=team.name) | Q(summary__contains=team.name))

        return Response(news.values('title', 'type__title', 'image_url', 'field',
                                    'created_date_time', 'slug')[0: int(num)])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def news_list_by_player(request, team_slug):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        news_list = News.objects.none()
        for player in PlayerTeam.objects.filter(teamLeague__team=team, deleted=False, ).values('player__name'):
            news_list = news_list | News.objects.\
                filter(Q(title__contains=player['player__name']) | Q(tags__title__contains=player['player__name']) |
                       Q(text__contains=player['player__name']) | Q(summary__contains=player['player__name']))

        return Response(news_list.values('title', 'type__title', 'image_url', 'field',
                                         'created_date_time', 'slug')[0: int(num)])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def slider_images(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        sliders = TeamSliderImage.objects.filter(team=team, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})


@api_view()
def info(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)
        team_info = team.values('name', 'image_url', 'nickname', 'internationalRank', 'city', 'country',
                                'establishedYear', 'coach', 'captain', 'website', 'field')
        return Response(team_info[0])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def members_list(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        members = PlayerTeam.objects.filter(teamLeague__team=team, teamLeague__league__active=True, deleted=False). \
            values('player__name', 'player__post__name', 'player__image_url', 'player__slug')
        return Response(members)
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def team_statistics(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        leagues = TeamLeague.objects.filter(team=team, league__active=False, deleted=False).values('league__name',
                                                                                                   'league__year',
                                                                                                   'result',
                                                                                                   'league__field')
        for league in leagues:
            league['game_number'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
                filter(Q(team1=team) | Q(team2=team)).count()

            league['win_num'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
                filter(Q(team1=team, team_state1='W') | Q(team2=team, team_state2='W')).count()

            league['lose_num'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
                filter(Q(team1=team, team_state1='L') | Q(team2=team, team_state2='L')).count()

            if league['league__field'] == 'FTB':
                league['scoring_goal_number'] = Goal.objects. \
                    filter(game__league__name=league['league__name'], deleted=False, scoring_team=team).count()

                league['receiving_goal_number'] = Goal.objects. \
                    filter(game__league__name=league['league__name'], deleted=False, receiving_team=team).count()

                league['draw_num'] = Game.objects.filter(league__name=league['league__name'], deleted=False). \
                    filter(Q(team1=team, team_state1='D') | Q(team2=team, team_state2='D')).count()

        return Response(leagues)
    except IndexError:
        return Response({})


@api_view()
def league_list(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        leagues = TeamLeague.objects.filter(team=team, league__active=True, deleted=False).values('league__name',
                                                                                                  'league__year',
                                                                                                  'league__field')
        for league in leagues:
            league['teams'] = TeamLeague.objects. \
                filter(league__name=league['league__name'], league__year=league['league__year']).values('team__name',
                                                                                                        'team__slug',
                                                                                                        'team__field')
            for team in league['teams']:
                team['game_number'] = Game.objects.filter(deleted=False, league__name=league['league__name'],
                                                          league__year=league['league__year']). \
                    filter(Q(team1__name=team['team__name']) | Q(team2__name=team['team__name'])).count()

                team['win_number'] = Game.objects.filter(deleted=False, league__name=league['league__name'],
                                                         league__year=league['league__year']). \
                    filter(Q(team1__name=team['team__name'], team_state1='W') |
                           Q(team2__name=team['team__name'], team_state2='W')).count()

                team['lose_number'] = Game.objects.filter(deleted=False, league__name=league['league__name'],
                                                          league__year=league['league__year']). \
                    filter(Q(team1__name=team['team__name'], team_state1='L') |
                           Q(team2__name=team['team__name'], team_state2='L')).count()
                if team['team__field'] == "FTB":
                    team['draw_number'] = Game.objects.filter(deleted=False, league__name=league['league__name'],
                                                              league__year=league['league__year']). \
                        filter(Q(team1__name=team['team__name'], team_state1='D') |
                               Q(team2__name=team['team__name'], team_state2='D')).count()

                    team['score'] = team['win_number'] * 3 + team['draw_number']

            if league['league__field'] == 'FTB':
                league['teams'] = sorted(league['teams'], key=lambda i: i['score'], reverse=True)
            else:
                league['teams'] = sorted(league['teams'], key=lambda i: i['win_number'], reverse=True)
            counter = 0
            for team in league['teams']:
                counter += 1
                team['rank'] = counter
        return Response(leagues)
    except IndexError:
        return Response({'h': 2})


@api_view()
def game_list(request, team_slug):
    try:
        state = request.GET.get('s')
        name = request.GET.get('n')

        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        if team.field == 'FTB':
            games = Game.objects.filter(Q(team1=team) | Q(team2=team)).values('team1__name', 'team2__name', 'full_time',
                                                                              'team1__image_url', 'team2__image_url',
                                                                              'goals1', 'goals2', 'game_date',
                                                                              'team1__slug', 'team2__slug', 'slug')
        else:
            games = Game.objects.filter(Q(team1=team) | Q(team2=team)).values('team1__name', 'team2__name', 'full_time',
                                                                              'team1__image_url', 'team2__image_url',
                                                                              'all_score1', 'all_score2', 'game_date',
                                                                              'team1__slug', 'team2__slug', 'slug')
        if state:
            games = games.filter(Q(team1=team, team_state1=state) | Q(team2=team, team_state2=state))
        if name:
            games = games.filter(Q(team1=team, team2__name=name), Q(team2=team, team2_name=name))

        return Response(games)
    except IndexError:
        return Response({})


@api_view()
def liking(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        user_id = Token.objects.filter(key__contains=request.data['token'])[0].user_id
        try:
            like = LikeTeam.objects.filter(user_id=user_id, team=team, deleted=False)[0]
            like.deleted = True
            like.save()
            return Response({'like': 'false'})
        except IndexError:
            try:
                like = LikeTeam.objects.filter(user_id=user_id, team=team, deleted=True)[0]
                like.deleted = False
                like.save()
                return Response({'like': 'true'})
            except IndexError:
                LikeTeam(user_id=user_id, team=team, created_date_time=timezone.now()).save()
                return Response({'like': 'true'})
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def like_check(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        user_id = Token.objects.filter(key__contains=request.data['token'])[0].user_id
        like = LikeTeam.objects.filter(user_id=user_id, team=team, deleted=False)[0]
        return Response({'like': 'True'})
    except (IndexError, AssertionError, OperationalError):
        return Response({'like': 'False'})
