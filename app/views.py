from rest_framework import generics

from . import models
from . serializers import NotificationSerializer


class NotificationListAPIView(generics.ListAPIView):
    queryset = models.Notification.objects.all().order_by('-id')
    serializer_class = NotificationSerializer
