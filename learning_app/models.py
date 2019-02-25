from django.db import models
from django.contrib.auth.models import  User
from datetime import datetime
# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete='cascade')


    last_seen = models.DateTimeField(blank=True, default = datetime.now)
    

    portfolio = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

class Note(models.Model):
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Sagar')

    def __str__(self):
        return self.text

class Memory(models.Model):
    desc = models.CharField(max_length=250)
    photo = models.ImageField()
    author = models.CharField(max_length=200, default='Sagar')

    created_at = models.DateTimeField(blank=True, default = datetime.now)
    likes = models.PositiveIntegerField(default=0)
