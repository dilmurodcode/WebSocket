from rest_framework import serializers
from . import models


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notification
        fields = (
            'id',
            'title',
            'description',
            'is_read',
            'created_at',
        )