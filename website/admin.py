from django.contrib import admin

from website.models.article import Article



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name','desc',  'date', 'tags',]

admin.site.register(Article, ArticleAdmin)

