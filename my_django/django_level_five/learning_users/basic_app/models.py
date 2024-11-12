from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # Create realationship (don't inherit from user!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portofolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # Create __str__ method to override the default one
    def __str__ (self):
        #Built-in atribute of django.contrib.auth.models.User
        return self.user.username