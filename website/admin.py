from django.contrib import admin

from website.models.article import Article
from website.models.profile import Profile



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','desc',  'date', 'tags',]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)

