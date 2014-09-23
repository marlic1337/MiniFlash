from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    title = models.CharField(max_length=128, blank=True)

    logo = models.ImageField(upload_to='logos', width_field='logo_width', height_field='logo_height', null=True, blank=True)
    logo_width = models.PositiveIntegerField(null=True)
    logo_height = models.PositiveIntegerField(null=True)

    def logo_url(self):
        if self.logo:
            return self.logo.url
        return settings.STATIC_URL + 'img/default_user.png'

class SocialNetworks(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True)

    url_facebook = models.CharField(max_length=64, blank=True)
    url_googleplus = models.CharField(max_length=64, blank=True)
    url_twitter = models.CharField(max_length=64, blank=True)
    url_linkedin = models.CharField(max_length=64, blank=True)
    url_github = models.CharField(max_length=64, blank=True)