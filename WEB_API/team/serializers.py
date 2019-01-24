from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'nickname', 'internatinalRank', 'city', 'country',
                  'establishedYear', 'coach', 'captain', 'website', 'created_date_time',
                  'image_url', 'field', 'url', 'tags', 'deleted']
