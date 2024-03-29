from django.contrib import admin
from webapp.models import Article, Comment, Category, Tag


class CommentAdmin(admin.TabularInline):
    model = Comment
    fields = ['author', 'text']
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'created_at']
    list_filter = ['author', 'category']
    list_display_links = ['pk', 'title']
    filter_horizontal = ['tags']
    search_fields = ['title', 'text']
    exclude = []
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CommentAdmin]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
