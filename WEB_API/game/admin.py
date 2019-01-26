from django.contrib import admin

from game.models import GameSliderImage, Game, GameReport, Goal, PenaltyGoal, YellowCard, RedCard, AssistGoal

admin.site.register(Game)
admin.site.register(GameSliderImage)
admin.site.register(GameReport)
admin.site.register(Goal)
admin.site.register(PenaltyGoal)
admin.site.register(YellowCard)
admin.site.register(RedCard)
admin.site.register(AssistGoal)
