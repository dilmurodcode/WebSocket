from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import NotificationSerializer

@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    print('SIGNAL WORKING')
    if created:
        channel_layer = get_channel_layer()
        data = NotificationSerializer(instance).data
        if not data['is_read']:
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    "type": "send_notification",
                    "content": data
                }
            )
