from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game, GameSliderImage, GameReport, Goal, RedCard, YellowCard, Substitute
from membership.models import PlayerGame, PlayerTeam
from news.models import News


@api_view()
def info(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)
        if game[0].field == 'FTB':
            game_state = game.values('team1__name', 'team2__name', 'team1__slug', 'team2__slug', 'team1__image_url',
                                     'team2__image_url', 'shots1', 'shots2', 'shots_on_target1', 'shots_on_target2',
                                     'possession1', 'possession2', 'passes1', 'passes2', 'fouls1', 'fouls2',
                                     'yellow_cards1', 'yellow_cards2', 'red_cards1', 'red_cards2', 'offsides1',
                                     'offsides2', 'corners1', 'corners2')
        else:
            game_state = game.values('team1__name', 'team2__name', 'team1__slug', 'team2__slug', 'team1__image_url',
                                     'team2__image_url', 'all_score1', 'all_score2', 'score1_team1', 'score1_team2',
                                     'score2_team1', 'score2_team2', 'score3_team1', 'score3_team2', 'ribbond1',
                                     'ribbond2', 'style1', 'style2', 'out1', 'out2', 'fouls1', 'fouls2',
                                     'counter_attack1', 'counter_attack2')

        return Response(game_state[0])
    except (IndexError, OperationalError):
        return Response({})


@api_view()
def newsList(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        tag_titles = game.tags.values_list('title')
        news = News.objects.filter(tags__title__in=tag_titles, deleted=False)
        return Response(news.values('title', 'type__title', 'image_url', 'created_date_time', 'slug'))
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


@api_view()
def player_list(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        players = {'team1': game.team1.name, 'team_slug_1': game.team1.slug, 'team_image_url1': game.team1.image_url,
                   'team2': game.team2.name, 'team_slug_2': game.team2.slug, 'team_image_url2': game.team2.image_url,
                   'fix_players1': PlayerGame.objects.filter(game=game, team=game.team1, fix=True, deleted=False).
                       values('player__slug', 'player__name', 'player__post__name'),
                   'fix_players2': PlayerGame.objects.filter(game=game, team=game.team2, fix=True, deleted=False).
                       values('player__slug', 'player__name', 'player__post__name'),
                   'substitute_player1': PlayerGame.objects.filter(game=game, team=game.team1, 
                                                                   fix=False, deleted=False).
                       values('player__slug', 'player__name', 'player__post__name'),
                   'substitute_player2': PlayerGame.objects.filter(game=game, team=game.team2,
                                                                   fix=False, deleted=False).
                       values('player__slug', 'player__name', 'player__post__name'),
                   }
        for player in players['fix_players1']:
            try:
                player['num'] = PlayerTeam.objects.filter(player__name=player['player__name'],
                                                          teamLeague__team__name=players['team1'],
                                                          teamLeague__league=game.league, )[0].num
                substitute = Substitute.objects.filter(game=game, deleted=False,
                                                       out_player__name=player['player__name'])
                if substitute is not None:
                    player['out_min'] = substitute[0].minute
                    player['out_sec'] = substitute[0].second
            except IndexError:
                pass

        for player in players['fix_players2']:
            try:
                player['num'] = PlayerTeam.objects.filter(player__name=player['player__name'],
                                                          teamLeague__team__name=players['team2'],
                                                          teamLeague__league=game.league, )[0].num
                substitute = Substitute.objects.filter(game=game, deleted=False,
                                                       out_player__name=player['player__name'])
                if substitute is not None:
                    player['out_min'] = substitute[0].minute
                    player['out_sec'] = substitute[0].second
            except IndexError:
                pass
        for player in players['substitute_player1']:
            try:
                player['num'] = PlayerTeam.objects.filter(player__name=player['player__name'],
                                                          teamLeague__team__name=players['team1'],
                                                          teamLeague__league=game.league)[0].num
                substitute_in = Substitute.objects.filter(game=game, deleted=False,
                                                           in_player__name=player['player__name'])

                substitute_out = Substitute.objects.filter(game=game, deleted=False,
                                                           out_player__name=player['player__name'])

                if substitute_in is not None:
                    player['in_min'] = substitute_in[0].minute
                    player['in_sec'] = substitute_in[0].second

                if substitute_in is not None:
                    player['out_min'] = substitute_out[0].minute
                    player['out_sec'] = substitute_out[0].second

            except IndexError:
                pass

        for player in players['substitute_player2']:
            try:
                player['num'] = PlayerTeam.objects.filter(player__name=player['player__name'],
                                                          teamLeague__team__name=players['team2'],
                                                          teamLeague__league=game.league, )[0].num
                substitute_in = Substitute.objects.filter(game=game, deleted=False,
                                                           in_player__name=player['player__name'])

                substitute_out = Substitute.objects.filter(game=game, deleted=False,
                                                           out_player__name=player['player__name'])

                if substitute_in is not None:
                    player['in_min'] = substitute_in[0].minute
                    player['in_sec'] = substitute_in[0].second

                if substitute_in is not None:
                    player['out_min'] = substitute_out[0].minute
                    player['out_sec'] = substitute_out[0].second

            except IndexError:
                pass

        return Response(players)
    except IndexError:
        return Response()


@api_view()
def time_lines(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        events = []
        goals = Goal.objects.filter(game=game, deleted=False, penalty=False).values('minute', 'second',
                                                                                    'scoring_team__name',
                                                                                    'receiving_team__name')

        penalty_goals = Goal.objects.filter(game=game, deleted=False, penalty=True).values('minute', 'second',
                                                                                           'scoring_team__name',
                                                                                           'receiving_team__name')

        red_cards = RedCard.objects.filter(game=game, deleted=False).values('minute', 'second', 'player__name',
                                                                            'team__name')

        yellow_cards = YellowCard.objects.filter(game=game, deleted=False).values('minute', 'second', 'player__name',
                                                                                  'team__name')

        substitutes = Substitute.objects.filter(game=game, deleted=False).values('in_player__name', 'out_player__name',
                                                                                 'minute', 'second', 'team__name')

        for goal in goals:
            goal['type'] = 'goal'
            events.append(goal)

        for penalty_goal in penalty_goals:
            penalty_goal['type'] = 'penalty goal'
            events.append(penalty_goal)

        for red_card in red_cards:
            red_card['type'] = 'red card'
            events.append(red_card)

        for yellow_card in yellow_cards:
            yellow_card['type'] = 'yellow card'
            events.append(yellow_card)

        for substitute in substitutes:
            substitute['type'] = 'substitute'
            events.append(substitute)

        events = sorted(events, key=lambda i: i['second'])
        events = sorted(events, key=lambda i: i['minute'])

        return Response(events)
    except IndexError:
        return Response()
