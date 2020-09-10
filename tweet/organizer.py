from twitteruser.models import CustomUserModel
from notification.models import NotificationModel
from tweet.models import TweetModel

import re  # http://rexegg.com/regex-quickstart.html


def tweet_parser(tweet):
    pattern = re.compile(r'(@)(\w+)(\s|$)')
    pattern_matched = pattern.search(tweet.characters)
    if pattern_matched:
        username = pattern_matched.group(2)
        user = CustomUserModel.objects.get(username=username)
        if user:
            NotificationModel.objects.create(tweet_notification=tweet, user_notification=user)
            return True
        return False


def the_tweet(tweet_id):
    return TweetModel.objects.filter(id=tweet_id)


#  https://docs.djangoproject.com/en/3.1/topics/db/queries/
def all_tweets(user_details):
    user_list = [user_details.id]
    for user_detail in user_details.follow.all():
        user_list.append(user_detail.id)
    tweets = TweetModel.objects.filter(user__id__in=user_list).order_by('datetime')
    return tweets


def tweets_byuser(user_details):
    return TweetModel.objects.filter(user__id=user_details.id).order_by('datetime')


def count_usertweets(user_details):
    return TweetModel.objects.filter(user__id=user_details.id).count()
