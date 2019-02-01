from django.contrib import admin

from game.models import GameSliderImage, Game, GameReport, Goal, YellowCard, RedCard, AssistGoal, Substitute, Throw, \
    Ribbond, Foul, AssistThrow

admin.site.register(Game)
admin.site.register(GameSliderImage)
admin.site.register(GameReport)
admin.site.register(Goal)
admin.site.register(YellowCard)
admin.site.register(RedCard)
admin.site.register(AssistGoal)
admin.site.register(Substitute)
admin.site.register(Throw)
admin.site.register(Ribbond)
admin.site.register(Foul)
admin.site.register(AssistThrow)
