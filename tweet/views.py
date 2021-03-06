from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from tweet.models import TweetModel
from tweet.forms import AddTweetForm
from tweet.organizer import tweet_parser


# Create your views here.
# @login_required
# def addtweet_view(request):
#     if request.method == 'POST':
#         addtweet_form = AddTweetForm(request.POST)
#         if addtweet_form.is_valid():
#             addtweet_data = addtweet_form.cleaned_data
#             tweet = TweetModel.objects.create(characters=addtweet_data.get('characters'), user=request.user)
#             tweet_parser(tweet)
#             return HttpResponseRedirect(reverse('homepage'))

#     addtweet_form = AddTweetForm()
#     return render(request, 'generic_form.html', {'page_title': 'TwitterClone', 'form': addtweet_form})


class AddTweetView(LoginRequiredMixin, TemplateView):
    
    def get(self, request):
        addtweet_form = AddTweetForm()
        return render(request, 'generic_form.html', {'page_title': 'TwitterClone', 'form': addtweet_form})
    
    def post(self, request):
        addtweet_form = AddTweetForm(request.POST)
        if addtweet_form.is_valid():
            addtweet_data = addtweet_form.cleaned_data
            tweet = TweetModel.objects.create(characters=addtweet_data.get('characters'), user=request.user)
            tweet_parser(tweet)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'generic_form.html', {'page_title': 'TwitterClone', 'form': addtweet_form})
