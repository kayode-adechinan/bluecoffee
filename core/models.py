from django.db import models

# Create your models here.
class Reporter(models.Model):
    name = models.CharField(max_length = 200, null=True)
    email = models.EmailField(null=True)
    password = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    picture = models.ImageField(upload_to='pictures/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
    like = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class FileHandler(models.Model):
    picture = models.ImageField(upload_to='pictures/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
