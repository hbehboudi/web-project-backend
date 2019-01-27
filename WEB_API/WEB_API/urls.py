from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

import news

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/accounts/', include('authentication.accounts.api.urls')),

    path('api/home/', include('home.urls')),
    path('api/team/', include('team.urls')),
    path('api/game/', include('game.urls')),
]
