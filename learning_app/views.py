from django.shortcuts import render
from learning_app.forms import UserForm, UserProfileForm

# necessary files for auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'learning_app/index.html')

# sign up logic
def register(request):
    registered = False
    # if the register button is clicked
    if request.method == "POST":
        # get all the data provided by the user
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # save the user and their profile
            user = user_form.save()
            # this where django hashes the password for us
            user.set_password(user.password)
            user.save()
            # photo is not saved to the db to check for other abnormalities
            profile = profile_form.save(commit=False)
            # set the user to a specific profile
            profile.user = user

            # if there is a profile picture uploaded
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            # save the entire profile
            profile.save()

            registered = True
        # if the form had errors
        else:
            print(user_form.errors, profile_form.errors)
    # if the user is new, a fresh form needs to be presented
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'learning_app/registration.html',
                    {
                        'user_form': user_form,
                        'profile_form': profile_form,
                        'registered': registered
                    })

# login logic
def user_login(request):
    # when the login button is clicked
    if request.method == 'POST':
        # get the username and password from the user
        username = request.POST.get('username')
        password = request.POST.get('password')

        # django authenticates the credentials
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # user is logged in and redirected to home page
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        # if there is no valid user
        else:
            print('someone tried to login with invalid credentials')
            return HttpResponse('Invalid username or password')
    # for someone trying to log in
    else:
        return render(request, 'learning_app/login.html', {})

@login_required
def user_logout(request):
    # logs out the user
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def feed(request):
    return render(request, 'learning_app/feed.html', {})
