from django.contrib import admin

from app.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_read', 'created_at')