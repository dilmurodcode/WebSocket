from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    class Meta:
        abstract = True


class Notification(BaseModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)