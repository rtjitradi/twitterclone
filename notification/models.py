from django.db import models

from twitteruser.models import CustomUserModel
from tweet.models import TweetModel


# Create your models here.
class NotificationModel(models.Model):
    tweet_notification = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    user_notification = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    new_notification = models.BooleanField(default=True)

    def __str__(self):
        return self.tweet_notification.characters
