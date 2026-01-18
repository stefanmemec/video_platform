from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = CloudinaryField(resource_type="video")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="videos"
    )

    def __str__(self):
        return self.title
