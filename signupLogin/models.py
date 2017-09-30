from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telephone = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=500, blank=True)
    birthday = models.DateField(default=datetime.date.today)
    bankaccount = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='userImage', blank=True)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()