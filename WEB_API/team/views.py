from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News
from team.models import Team
from membership.models import PlayerTeam


@api_view()
def memberList(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        members = PlayerTeam.objects.filter(teamLeague__team=team, teamLeague__active=True, deleted=False).values(
            'player__name', 'player__post', 'player__image_url', 'player__slug')
        return Response(members)
    except IndexError:
        return Response({})


@api_view()
def newsList(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        tag_titles = team.tags.values_list('title')
        news = News.objects.filter(tags__title__in=tag_titles, deleted=False)
        return Response(news.values('title', 'category', 'image_url', 'field', 'created_date_time', 'slug'))
    except IndexError:
        return Response({})
