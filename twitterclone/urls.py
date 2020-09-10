"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from twitteruser import views as twitteruserviews
from tweet import views as tweetviews
from authentication import views as authenticationviews
# https://stackoverflow.com/questions/56351141/why-i-have-issues-in-importing-views-in-the-urls-py-file

urlpatterns = [
    path('', twitteruserviews.index_view, name='homepage'),
    path('signup/', authenticationviews.signup_view, name='signup'),
    path('login/', authenticationviews.login_view, name='login'),
    path('logout/', authenticationviews.logout_view, name='logout'),
    path('addtweet/', tweetviews.addtweet_view, name='addtweet'),
    path('tweetdetails/<int:tweet_id>/', twitteruserviews.tweet_view, name='tweetdetails'),
    path('userprofile/<str:user_username>/', twitteruserviews.userprofile_view, name='userprofile'),
    path('notifications/<str:user_username>/', twitteruserviews.notifications_view, name='notifications'),
    path('follow/<str:user_username>/', twitteruserviews.follow_view, name='follow'),
    path('unfollow/<str:user_username>/', twitteruserviews.unfollow_view, name='unfollow'),
    path('admin/', admin.site.urls),
]
