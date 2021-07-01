from django.db.models.signals import post_save
# above import sends a signal everytime a save happens

from django.contrib.auth.models import User
# imported this as this will send a signal when user is created
from django.dispatch import receiver
# this will recive the signal
from .models import Profile
# needed to be imported as we need to create a profile when a signal is sent

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#add signals to apps.py