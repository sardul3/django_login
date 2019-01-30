from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete='cascade')

    portfolio = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
