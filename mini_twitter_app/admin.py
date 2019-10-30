from django.contrib import admin

from mini_twitter_app.models import *


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['username', ]
    list_display = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'location', 'tweets', ]

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    def tweets(self, obj):
        return obj.user.user_tweets.all().count()


class TweetAdmin(admin.ModelAdmin):
    list_display = ['username', 'tweet', 'mentions', 'replies', 'published', ]

    def username(self, obj):
        return obj.user.username

    def mentions(self, obj):
        mentions = obj.mentions.all()
        return mentions.count() if mentions else 0

    def replies(self, obj):
        return obj.replies.all().count()


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserConfig)
admin.site.register(Tweet, TweetAdmin)
