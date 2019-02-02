from django.db import OperationalError
from django.db.models import Q
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from game.models import Substitute, Goal, Throw, Foul, Ribbond, YellowCard, RedCard, AssistGoal, AssistThrow
from membership.models import PlayerTeam, PlayerGame
from news.models import News
from player.models import Player, PlayerSliderImage, LikePlayer


@api_view()
def news_list(request, player_slug):
    try:
        num = request.GET.get('n')
        if num is None:
            num = 10
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        news = News.objects.filter(Q(title__contains=player.name) | Q(tags__title__contains=player.name) |
                                   Q(text__contains=player.name) | Q(summary__contains=player.name))
        return Response(news.values('title', 'type__title', 'image_url', 'field',
                                    'created_date_time', 'slug')[0: int(num)])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def info(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)
        player_info = player.values('name', 'image_url', 'post__name', 'field', 'age', 'birth_place', 'height',
                                    'nationality', 'team', 'weight', 'teamNum', 'nationalityTeamNum', 'website', 'slug')
        return Response(player_info[0])
    except (IndexError, AssertionError, OperationalError):
        return Response({})


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
                                                                                 'teamLeague__league__year',
                                                                                 'teamLeague__league__slug',
                                                                                 'player__field')

        for league in leagues:
            player_team = PlayerTeam.objects.filter(player=player, deleted=False,
                                                    teamLeague__league__name=league['teamLeague__league__name'],
                                                    teamLeague__league__year=league['teamLeague__league__year'])

            league['team'] = player_team[0].teamLeague.team.name

            league['team_slug'] = player_team[0].teamLeague.team.slug

            league['num'] = player_team[0].num

            league['game_num'] = PlayerGame.objects.\
                                     filter(player=player, team__name=league['team'], deleted=False,
                                            game__league__name=league['teamLeague__league__name'],
                                            game__league__year=league['teamLeague__league__year']).count() + \
                                 Substitute.objects.\
                                     filter(in_player=player, team__name=league['team'], deleted=False,
                                            game__league__name=league['teamLeague__league__name'],
                                            game__league__year=league['teamLeague__league__year']).count()
            league['time'] = 0
            for time in PlayerGame.objects.filter(player=player, deleted=False, team__name=league['team'],
                                                  game__league__name=league['teamLeague__league__name'],
                                                  game__league__year=league['teamLeague__league__name']). \
                    values('time'):
                league['time'] = time + league['time']

            if player.field == "FTB":
                league['scoring_goal_number'] = Goal.objects. \
                    filter(player=player, deleted=False, penalty=False, own_goal=False,
                           game__league__name=league['teamLeague__league__name'], scoring_team__name=league['team'],
                           game__league__year=league['teamLeague__league__year']).count()
                league['scoring_penalty_goal_number'] = Goal.objects. \
                    filter(player=player, deleted=False, scoring_team__name=league['team'], penalty=True,
                           own_goal=False, game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__year']).count()
                league['yellow_card_number'] = YellowCard.objects. \
                    filter(player=player, deleted=False, team__name=league['team'],
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__year']).count()
                league['red_card_number'] = RedCard.objects. \
                    filter(player=player, deleted=False, team__name=league['team'],
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__year']).count()
                league['assist_goal_number'] = AssistGoal.objects. \
                    filter(player=player, deleted=False, goal__scoring_team__name=league['team'],
                           goal__game__league__name=league['teamLeague__league__name'],
                           goal__game__league__year=league['teamLeague__league__year']).count()
            else:
                league['throw1_number'] = Throw.objects.\
                    filter(player=player, deleted=False, team__name=league['team'], score="1",
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__name']).count()
                league['throw2_number'] = Throw.objects.\
                    filter(player=player, deleted=False, team__name=league['team'], score="2",
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__name']).count()
                league['throw3_number'] = Throw.objects. \
                    filter(player=player, deleted=False, team__name=league['team'], score="3",
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__name']).count()
                league['all_score'] = 3 * league['throw3_number'] +\
                                      2 * league['throw2_number'] * league['throw1_number']
                league['assist_number'] = AssistThrow.objects.\
                    filter(player=player, deleted=False, team__name=league['team'],
                           throw__game__league__name=league['teamLeague__league__name'],
                           throw__game__league__year=league['teamLeague__league__name']).count()
                league['foul_number'] = Foul.objects. \
                    filter(player=player, deleted=False, team__name=league['team'],
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__name']).count()
                league['ribbond'] = Ribbond.objects. \
                    filter(player=player, deleted=False, team__name=league['team'],
                           game__league__name=league['teamLeague__league__name'],
                           game__league__year=league['teamLeague__league__name']).count()

        return Response(leagues)
    except IndexError:
        return Response({})


@api_view()
def liking(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        user_id = Token.objects.filter(key__contains=request.data['token'])[0].user_id
        try:
            like = LikePlayer.objects.filter(user_id=user_id, player=player, deleted=False)[0]
            like.deleted = True
            like.save()
            return Response({'like': 'false'})
        except IndexError:
            try:
                like = LikePlayer.objects.filter(user_id=user_id, player=player, deleted=True)[0]
                like.deleted = False
                like.save()
                return Response({'like': 'true'})
            except IndexError:
                LikePlayer(user_id=user_id, player=player, created_date_time=timezone.now()).save()
                return Response({'like': 'true'})
    except (IndexError, AssertionError, OperationalError):
        return Response({})


@api_view()
def like_check(request, player_slug):
    try:
        player = Player.objects.filter(slug__contains=player_slug, deleted=False)[0]
        user_id = Token.objects.filter(key__contains=request.data['token'])[0].user_id
        like = LikePlayer.objects.filter(user_id=user_id, player=player, deleted=False)[0]
        return Response({'like': 'True'})
    except (IndexError, AssertionError, OperationalError):
        return Response({'like': 'False'})
