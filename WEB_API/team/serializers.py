from rest_framework import serializers

from player.models import Player
from team.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'nickname', 'internatinalRank', 'city', 'country', 'establishedYear', 'coach', 'captain',
                  'website', 'created_date_time', 'image_url', 'field', 'slug', 'tags', 'deleted']
        lookup_field = 'slug'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'post']
