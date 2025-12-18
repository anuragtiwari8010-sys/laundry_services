from django.contrib import admin
from django.utils.html import format_html
from .models import Ourguards


class OurguardsAdmin(admin.ModelAdmin):
    list_display = ('Ourguards_person', 'Ourguards_post', 'img_preview', 'file_link', 'created_at')
    search_fields = ('Ourguards_person', 'Ourguards_post')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)

    def img_preview(self, obj):
        if obj.Ourguards_img:
            return format_html("<img src='{}' style='height:60px;border-radius:4px;'/>", obj.Ourguards_img.url)
        return '-'
    img_preview.short_description = 'Image'

    def file_link(self, obj):
        if obj.Ourguards_file:
            return format_html("<a href='{}' target='_blank'>Download</a>", obj.Ourguards_file.url)
        return '-'
    file_link.short_description = 'File'


admin.site.register(Ourguards, OurguardsAdmin)
