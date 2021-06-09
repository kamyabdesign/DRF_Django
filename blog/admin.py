from django.contrib import admin

from . models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_display_links = ('title', 'slug')


admin.site.register(Article, ArticleAdmin)
