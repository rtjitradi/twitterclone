from twitteruser.models import CustomUserModel
from notification.models import NotificationModel
from tweet.organizer import the_tweet, all_tweets, tweets_byuser, count_usertweets
from notification.organizer import all_notifications, delete_notification, count_notifications

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required


# Thank you for the study halls. Special thanks to Matt and Howard for the guidance.
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
        'page_title': 'TwitterClone: Tweet Details',
        'template_name': 'tweets.html',
        'tweet': tweet
    })


def userprofile_view(request, user_username):
    user_details = CustomUserModel.objects.get(username=user_username)
    tweets = all_tweets(user_details)
    follows_count = user_details.follow.all().count()
    usertweets_count = count_usertweets(user_details)
    notifications_count = count_notifications(user_details)
    return render(request, 'userprofile.html', {
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
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def unfollow_view(request, user_username):
    user = CustomUserModel.objects.get(username=user_username)
    request.user.follow.remove(user)
    return HttpResponseRedirect(reverse('homepage'))


def notifications_view(request, user_username):
    # Guided by Matt: For notifications we want to show who mentioned us by using @syntax, so we filter it and request the user in the first filter argument
    notifiers = NotificationModel.objects.filter(user_notification=request.user).filter(new_notification=True)
    # Also, we want to have a second filter on the notifiers since we only want the newest notifier in notification. By viewing it, it automatically convert it to older notification thus erasing it
    # In order to do this we need to itirate through the notifiers and set the old notifier to false by setting it to false (the default for new notification per model set to True, so when we changed it to False it became old)
    for notifier in notifiers:
        notifier.new_notification = False
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
        'tweets': notifiers,
        'usertweets_count': usertweets_count,
        'notification_all': notifications_all,
        'notification_delete': notification_delete,
        'notification_count': notifications_count
    })
