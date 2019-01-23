from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

import news

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^api/accounts/', include('authentication.accounts.api.urls')),

    # url(r'^api/teams/', include('authentication.teams.api.urls')),

    path('news/', include('news.urls'))
]
