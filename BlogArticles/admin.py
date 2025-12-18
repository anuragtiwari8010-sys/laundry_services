from django.contrib import admin
from BlogArticles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'views')
    search_fields = ('title', 'author', 'category')
    list_filter = ('created_at', 'category')
    readonly_fields = ('created_at', 'updated_at', 'views')
    fieldsets = (
        ('Article Info', {
            'fields': ('title', 'author', 'category', 'featured_image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Meta', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Article, ArticleAdmin)
