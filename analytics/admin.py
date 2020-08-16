from django.contrib import admin

from .models import ObjectViewed, UserSession


class ObjectViewedAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'content_object', 'timestamp']
    list_filter = ['user']
    search_fields = ['user']


admin.site.register(ObjectViewed, ObjectViewedAdmin)
admin.site.register(UserSession)
