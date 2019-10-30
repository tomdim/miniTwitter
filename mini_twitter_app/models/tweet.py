from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tweets')
    tweet = models.TextField(blank=False, null=False)
    reply_to = models.ForeignKey('mini_twitter_app.Tweet', blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name='replies')
    mentions = models.ManyToManyField(User, blank=True, related_name='mentioned_to')

    # comma separated tags
    hashtags = models.TextField(blank=True, null=True)

    # image = models.ImageField()

    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.tweet, self.user.username)
