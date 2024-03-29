from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


class Post(models.Model):
    title = models.TextField(max_length=50, default='')
    cover = models.ImageField(upload_to='images/mens/')

    def __str__(self):
        return self.title
