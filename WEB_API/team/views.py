from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News
from team.models import Team, TeamSliderImage
from membership.models import PlayerTeam


@api_view()
def members_list(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        members = PlayerTeam.objects.filter(teamLeague__team=team, teamLeague__active=True, deleted=False).values(
            'player__name', 'player__post', 'player__image_url', 'player__slug')
        return Response(members)
    except IndexError:
        return Response({})


@api_view()
def news_list(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        tag_titles = team.tags.values_list('title')
        news = News.objects.filter(tags__title__in=tag_titles, deleted=False)
        return Response(news.values('title', 'category', 'image_url', 'field', 'created_date_time', 'slug'))
    except IndexError:
        return Response({})


@api_view()
def info(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        team_info = team.values('name', 'image_url', 'internationalRank', 'city', 'country', 'establishedYear', 'coach',
                                'website')
        return Response(team_info[0])
    except (IndexError, OperationalError):
        return Response({})


@api_view()
def slider_images(request, team_slug):
    try:
        team = Team.objects.filter(slug__contains=team_slug, deleted=False)[0]
        sliders = TeamSliderImage.objects.filter(team=team, deleted=False).values('title', 'image_url')
        return Response(sliders)
    except IndexError:
        return Response({})

