from django.contrib import admin

from website.models.article import Article
from website.models.profile import Profile
from website.models.project import Project



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','desc',  'date', 'tags',]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', ]

class ProjectCustom(admin.ModelAdmin):
    list_display = ['name','display',  'description', 'image',]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectCustom)
