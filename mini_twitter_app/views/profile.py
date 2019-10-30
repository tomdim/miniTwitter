from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mini_twitter_app.forms import SignUpForm


def signup(request):
    if request.method == 'POST':

        # get form
        form = SignUpForm(request.POST)

        # validate form
        if form.is_valid():

            # save user
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal

            # set birth date
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('explore')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
