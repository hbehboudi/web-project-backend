import slug as slug
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from player.models import Player
from player_in_team.models import PlayerTeam
from team.models import Team
from team.serializers import TeamSerializer, MemberSerializer


# class TeamViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer
#     lookup_field = 'slug'

class MemberListAPIView(generics.ListAPIView):
    serializer_class = MemberSerializer
    lookup_field = 'name'

    def get_queryset(self):
        return PlayerTeam.objects.filter(active=True)


@api_view()
def memberList(request, slug):
    team = Team.objects.filter(slug__contains=slug)[0]
    playerTeam = PlayerTeam.objects.filter(team=team, active=True).values('player__name', 'player__post')
    return Response(playerTeam)



#
# def user_home(request):
#     p = request.GET.get('p')
#     user = request.user
#     relations = Relation.objects.filter(follower_id=user.id).values_list('followed_by_id', flat=True)
#     posts = Post.objects.filter(owner_id__in=relations, deleted=False).values('id', 'content')
#     if p:
#         p = int(p)
#         posts = posts[10 * (p - 1): 10 * p]
#     return render(request, 'faceapp/user_home.html', {'posts': posts})
#
#
#
#
# def user_posts(request, username):
#     q = request.GET.get('qs')
#     ex = request.GET.get('ex')
#     # user = get_object_or_404(User, username=username)
#     all_posts = Post.objects.filter(owner__username=username).prefetch_related(Prefetch('comments', queryset=Comment.objects.filter(deleted=False).annotate(no_of_likes=Count('likes')), to_attr='all_comments')).annotate(no_of_likes=Count('likes'))
#     all_likes = all_posts.aggregate(all_likes=Sum('no_of_likes'))
#     print(all_likes)
#     # print(all_posts['all_likes'])
#
#     if q:
#         all_posts = all_posts.filter(content__icontains=q)
#     if ex:
#         all_posts = all_posts.exclude(content__icontains=ex)
#     return render(request, 'faceapp/posts.html', {'posts': all_posts})
#
#
# # def user_posts_search(request, username, query):
# #     # user = get_object_or_404(User, username=username)
# #     all_posts = Post.objects.filter(owner__username=username, content__icontains=query).prefetch_related('comments')
# #     return render(request, 'faceapp/posts.html', {'posts': all_posts})
