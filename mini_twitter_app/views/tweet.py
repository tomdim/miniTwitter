import json

from django.shortcuts import redirect

from mini_twitter_app.models import Tweet


def tweet(request):

    if request.method == 'POST':
        tweet_text = request.POST.get('tweet', '').strip()

        if tweet_text:
            Tweet.objects.create(
                tweet=tweet_text,
                user=request.user
            )

    return redirect('explore')


