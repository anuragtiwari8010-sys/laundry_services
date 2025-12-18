from django.contrib import admin
from ourservice.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_desc', 'service_read_link')
    search_fields = ('service_title',)


admin.site.register(Service, ServiceAdmin)
