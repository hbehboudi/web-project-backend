# import uuid
#
# from django.db import models
#
# # Create your models here.
# from rest_framework import serializers, generics
#
#
# class Tag(models.Model):
#     tag = models.CharField(primary_key=True, max_length=32)
#
#     def __str__(self):
#         return self.tag
#
#
# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('tag')
#
#
# class News(models.Model):
#     FIELDS = (
#         ('FTB', 'Football'),
#         ('BSK', 'Basketball'),
#         ('OTH', 'Other')
#     )
#
#     title = models.CharField(max_length=128)
#     category = models.CharField(max_length=16, null=True)
#     date = models.DateTimeField()
#     image_url = models.URLField()
#     text = models.CharField(max_length=4096)
#     field = models.CharField(max_length=3, choices=FIELDS, default='OTH')
#     url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
#     tags = models.ManyToManyField(Tag)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ('date',)
#
#
# class Tournament(models.Model):
#     name = models.CharField(max_length=128)
#     image_1 = models.URLField()
#     image_2 = models.URLField()
#
#
# class Competition(models.Model):
#     name = models.CharField(max_length=64)
#     complete_name = models.CharField(max_length=128)
#     year = models.IntegerField()
#     tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
#     pass
#
#
# class Team(models.Model):
#     name = models.CharField(max_length=64)
#     complete_name = models.CharField(max_length=128)
#     current_tournaments = models.ManyToManyField(Competition)
#     url = models.SlugField()
#     logo = models.URLField()
#     image_1 = models.URLField()
#     image_2 = models.URLField()
#     image_3 = models.URLField()
#
#     pass
#
#
# class Person(models.Model):
#     POSITION = (
#         (11, 'HEAD_COACH'),
#         (12, 'COACH'),
#         (13, 'GOALKEEPER'),
#         (14, 'DEFENDER'),
#         (15, 'MIDFIELDER'),
#         (16, 'STRIKER'),
#         (21, 'SHOOTING_GUARD'),
#         (22, 'POINT_GUARD'),
#         (23, 'POWER_FORWARD'),
#         (24, 'SMALL_FORWARD'),
#         (25, 'CENTER')
#
#     )
#     name = models.CharField(max_length=64)
#     complete_name = models.CharField(max_length=128)
#     position = models.IntegerField(choices=POSITION)
#     url = models.SlugField()
#     club = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='person_team')
#     national_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='person_national_team')
#     club_number = models.IntegerField()
#     national_team_number = models.IntegerField()
#     image_avatar = models.URLField()
#     image_1 = models.URLField(null=True)
#     image_2 = models.URLField()
#     image_3 = models.URLField()
#     pass
#
#
# class Match(models.Model):
#     competition = models.ForeignKey(Competition, on_delete=models.DO_NOTHING)
#     date = models.DateTimeField()
#     level = models.CharField(max_length=16)
#     home = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='match_home_team', null=True)
#     away = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='match_away_team', null=True)
#     url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
#
#
# class Goal(models.Model):
#     scoring_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='goal_scoring_team')
#     receiving_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='goal_receiving_team')
#     scorer = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='goal_scorer')
#     minute = models.IntegerField()
#     assist = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='goal_assist')
#     penalty = models.BooleanField()
#
#
# class Injury(models.Model):
#     player = models.ForeignKey(Person, on_delete=models.CASCADE)
#     minute = models.IntegerField()
#     match = models.ForeignKey(Match, on_delete=models.CASCADE)
#
#
# class Booking(models.Model):
#     COLOR = (
#         (1, 'yellow'),
#         (2, 'red')
#     )
#     given_to = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
#     match = models.ForeignKey(Match, on_delete=models.DO_NOTHING)
#     color = models.IntegerField(choices=COLOR)
#     minute = models.IntegerField()
#
#
# class Substitution(models.Model):
#     player_in = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='player_in')
#     player_out = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='player_out')
#     match = models.ForeignKey(Match, on_delete=models.CASCADE)
#     minute = models.IntegerField()
#
#
# class NewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = News
#         fields = ('title', 'category', 'date', 'image_url', 'text', 'field', 'tags')
#         depth = 1
#
#
# class NewsList(generics.ListCreateAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
