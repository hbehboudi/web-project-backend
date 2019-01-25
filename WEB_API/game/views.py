from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from game.models import Game


@api_view()
def state(request, game_slug):
    try:
        game = Game.objects.filter(slug__contains=game_slug, deleted=False)[0]
        game_state = game.values('team1__name', 'team1__name', 'team1__image_url', 'team2__image_url', 'shots1',
                                 'shots2', 'shots_on_target1', 'shots_on_target2', 'possession1', 'possession2',
                                 'passes1', 'passes2', 'fouls1', 'fouls2', 'yellow_cards1', 'yellow_cards2',
                                 'red_cards1', 'red_cards2', 'offsides1', 'offsides2', 'corners1', 'corners2')
        return Response(game_state)
    except (IndexError, OperationalError):
        return Response({})
