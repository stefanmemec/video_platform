###from django.db import models
##from django.contrib.auth.models import User

##class Video(models.Model):
 ##   user = models.ForeignKey(User, on_delete=models.CASCADE)
  ###  title = models.CharField(max_length=100)
  ##  description = models.TextField(blank=True)
  ##  file = models.FileField(upload_to='videos/')
  ##  uploaded_at = models.DateTimeField(auto_now_add=True)

  ##  def __str__(self):
  ##      return self.title
###


from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # секое видео припаѓа на еден корисник
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = CloudinaryField('video')  # Cloudinary field за upload
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
