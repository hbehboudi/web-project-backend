from django.contrib import admin

from membership.models import TeamLeague, PlayerTeam, PlayerGame

admin.site.register(TeamLeague)
admin.site.register(PlayerTeam)
admin.site.register(PlayerGame)
