from twitteruser.models import CustomUserModel
from tweet.organizer import the_tweet, all_tweets, tweets_byuser, count_usertweets
from notification.organizer import all_notifications, delete_notification, count_notifications

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Thank you for the study halls and especially Howard for the guidance.
# Create your views here.
@login_required
def index_view(request):
    user_details = CustomUserModel.objects.get(id=request.user.id)
    tweets = all_tweets(user_details)
    follows_count = user_details.follow.all().count()
    usertweets_count = count_usertweets(user_details)
    notifications_count = count_notifications(user_details)
    return render(request, 'index.html', {
        'page_title': 'TwitterClone: Homepage',
        'template_name': 'tweets.html',
        'user_details': user_details,
        'follows_count': follows_count,
        'tweets': tweets,
        'usertweets_count': usertweets_count,
        'notifications_count': notifications_count
    })


def tweet_view(request, tweet_id):
    tweet = the_tweet(tweet_id)
    return render(request, 'index.html', {
        'page_title': 'TwitterClone: All Tweets',
        'template_name': 'tweets.html',
        'tweet': tweet
    })


def userprofile_view(request, user_username):
    user_details = CustomUserModel.objects.get(username=user_username)
    tweets = all_tweets(user_details)
    follows_count = user_details.follow.all().count()
    usertweets_count = count_usertweets(user_details)
    notifications_count = count_notifications(user_details)
    return render(request, 'index.html', {
        'page_title': 'TwitterClone: User Profile',
        'template_name': 'tweets.html',
        'user_details': user_details,
        'tweets': tweets,
        'follows_count': follows_count,
        'usertweets_count': usertweets_count,
        'notifications_count': notifications_count
    })


@login_required
def follow_view(request, user_username):
    user = CustomUserModel.objects.get(username=user_username)
    request.user.follow.add(user)
    return redirect('/' + user.username + '/')


@login_required
def unfollow_view(request, user_username):
    user = CustomUserModel.objects.get(username=user_username)
    request.user.follow.remove(user)
    return redirect('/' + user.username + '/')


def notifications_view(request, user_username):
    user_details = CustomUserModel.objects.get(username=user_username)
    follows_count = user_details.follow.all().count()
    tweets = tweets_byuser(user_details)
    usertweets_count = count_usertweets(user_details)
    notifications_all = all_notifications(user_details)
    notification_delete = delete_notification(user_details)
    notifications_count = count_notifications(user_details)
    return render(request, 'index.html', {
        'page_title': 'TwitterClone: Notifications',
        'template_name': 'notifications.html',
        'user_details': user_details,
        'follows_count': follows_count,
        'tweets': tweets,
        'usertweets_count': usertweets_count,
        'notification_all': notifications_all,
        'notification_delete': notification_delete,
        'notification_count': notifications_count
    })
