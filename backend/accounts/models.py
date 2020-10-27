from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.api.models import TvInfo


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField("Description",blank=True, null=True)
    location = models.CharField("Location", max_length=30, blank=True)
    channels = models.ManyToManyField(TvInfo, blank=True)
    date_joined = models.DateTimeField("Joined Date", auto_now_add=True)
    updated_on = models.DateTimeField("Updated Date", auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])