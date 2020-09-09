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

from twitteruser import views
from tweet import views
from authentication import views
# https://stackoverflow.com/questions/56351141/why-i-have-issues-in-importing-views-in-the-urls-py-file

urlpatterns = [
    path('', views.index_view, name='homepage'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('addtweet/', views.addtweet_view, name='addtweet'),
    path('tweetdetails/<int:tweet_id>/', views.tweet_view, name='tweetdetails'),
    path('<str:user_username>/', views.userprofile_view, name='userprofile'),
    path('notifications/<str:user_username>/', views.notifications_view, name='notifications'),
    path('<str:user_username>/', views.follow_view, name='follow'),
    path('<str:user_username>/', views.unfollow_view, name='unfollow'),
    path('admin/', admin.site.urls),
]
