from django.urls import path
from . import views


urlpatterns = [
    path('notification-list/', views.NotificationListAPIView.as_view()),
]