from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','published_date', 'author')
    list_display_links = ('id','title')
    list_perpage = 25


admin.site.register(Article, ArticleAdmin)