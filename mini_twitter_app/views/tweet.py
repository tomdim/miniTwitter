from django.shortcuts import render, redirect
from mini_twitter_app.forms import TweetForm


def tweet(request):
    data = request.POST

    tweet = data.get('tweet', None)


