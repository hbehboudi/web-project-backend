from django.contrib import admin

from game.models import GameSliderImage, Game, GameReport

admin.site.register(Game)
admin.site.register(GameSliderImage)
admin.site.register(GameReport)
