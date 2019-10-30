from django.shortcuts import render

from mini_twitter_app.models import *


def explore(request, page=1):
    # get request data (GET)
    data = request.GET
    # get requested page
    page = int(data.get('page', '1'))
    # if no page is specified, return the first page
    page = 1 if page < 1 else page
    # number of tweets per page
    page_size = 5

    # get all tweets ordered by publish date descending (newest to oldest)
    tweets = Tweet.objects.all().order_by('-published')

    # paginate tweets
    tweets = tweets[(page - 1) * page_size: page * page_size]

    # get the number of tweets -- slow on large number of tweets! (see reltuples)
    tweets_count = tweets.count()

    # calculate number of pages
    pages = int(tweets_count / page_size) + 1

    return render(request, 'explore.html', {
        'tweets': tweets,
        'count': tweets_count,
        'pages': {
            'total': pages,
            'current': page,
        },
    })
