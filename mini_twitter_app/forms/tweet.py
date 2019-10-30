from django import forms
from mini_twitter_app.models import Tweet


class TweetForm(forms.ModelForm):
    tweet = forms.TextInput()

    class Meta:
        model = Tweet
        fields = ('tweet', )
