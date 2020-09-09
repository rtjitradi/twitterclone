from django.db import models
from django.utils import timezone

from twitteruser.models import CustomUserModel


# Create your models here.
class TweetModel(models.Model):
    characters = models.CharField(max_length=140)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.characters
