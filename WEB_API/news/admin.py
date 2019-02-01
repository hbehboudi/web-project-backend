from django.contrib import admin

from news.models import News, NewsType, Comment

admin.site.register(News)
admin.site.register(NewsType)
admin.site.register(Comment)
