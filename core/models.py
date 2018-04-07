from django.db import models
import cloudinary
import cloudinary.uploader

# Create your models here.
class Reporter(models.Model):
    name = models.CharField(max_length = 200, null=True)
    email = models.EmailField(null=True)
    password = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    avatar_url = models.TextField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.avatar:
            rci = cloudinary.uploader.upload(self.avatar)
            self.avatar_url = rci['url']
            self.avatar = None

        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    picture = models.ImageField(upload_to='pictures/', null=True)
    picture_url = models.TextField(null=True)
    video = models.FileField(upload_to='videos/', null=True)
    video_url = models.TextField(null=True)
    like = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        rci = cloudinary.uploader.upload(self.picture)
        self.picture_url = rci['url']
        self.picture = None

        rcv = cloudinary.uploader.upload(self.video, resource_type='video', format='mp4')
        self.video_url = rcv['url']
        self.video = None

        super().save(*args, **kwargs)


class FileHandler(models.Model):
    picture = models.ImageField(upload_to='pictures/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
