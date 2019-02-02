from django.contrib import admin

from player.models import PlayerSliderImage, Player, PlayerPost, LikePlayer

admin.site.register(Player)
admin.site.register(PlayerSliderImage)
admin.site.register(PlayerPost)
admin.site.register(LikePlayer)
