from django.contrib import admin
from contactFrom.models import Contact
from django.utils.html import format_html


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'attachment_link', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)

    def attachment_link(self, obj):
        if obj.attachment:
            return format_html("<a href='{}' target='_blank'>Download</a>", obj.attachment.url)
        return '-'
    attachment_link.short_description = 'Attachment'


admin.site.register(Contact, ContactAdmin)
