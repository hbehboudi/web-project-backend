from django.contrib import admin

from player.models import PlayerSliderImage, Player, PlayerPost

admin.site.register(Player)
admin.site.register(PlayerSliderImage)
admin.site.register(PlayerPost)
