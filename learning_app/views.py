from django.shortcuts import render, redirect
from learning_app.forms import UserForm, UserProfileForm, MemoryForm

# necessary files for auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Note, Memory, UserProfileModel, Forum
import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.messages import get_messages
# Create your views here.
def index(request):



    memories = Memory.objects.all()
    context = {'memories':memories}
    return render(request, 'learning_app/index.html', context)

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
            messages.success(request, 'Successfuly registered')
            return render(request, 'learning_app/login.html')
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
                messages.success(request, 'You are now logged in')
                return HttpResponseRedirect(reverse('feed'))
            else:
                return HttpResponse('Account is not active')
        # if there is no valid user
        else:
            messages.error(request, 'Invalid username / password')
            return HttpResponseRedirect(reverse('learning_app:user_login'))

    # for someone trying to log in
    else:
        return HttpResponseRedirect(reverse('learning_app:feed'))

@login_required
def user_logout(request):
    # logs out the user
    logout(request)
    messages.error(request, 'successfuly logged out')
    return HttpResponseRedirect(reverse('info'))

@login_required
def feed(request):
    form = MemoryForm(request.POST, request.FILES)

    if request.method == "POST":

        if form.is_valid():
            form.save()
        else:
            form = MemoryForm()

    note = Note.objects.filter(author=request.user.username)
    memories = Memory.objects.filter(author=request.user.username)
    print(request.user.username)
    profile_user = UserProfileModel.objects.get(user=request.user)
    profile_photo = profile_user.profile_picture
    context = {'user': request.user, 'note': note, 'form': form, 'memories':memories, 'profile_photo': profile_photo, 'user': profile_user}

    return render(request, 'learning_app/feed.html', context)

def add(request):
    note_text = request.POST.get('note_text')
    n = Note(text=note_text, author = request.user.username)
    n.save()
    context = {'note': n}
    messages.success(request, 'Note added successfuly')
    return HttpResponseRedirect(reverse('feed'), context)

def delete_note(request, note_id):
    n = Note.objects.get(pk=note_id)
    n.delete()
    messages.warning(request, 'You deleted a note')
    return HttpResponseRedirect(reverse('feed'))


def list_users(request):
    users = UserProfileModel.objects.all()
    context = {'users': users}
    return render(request, 'learning_app/users.html', context)

def view_profile(request, user_id):
    profile_user = UserProfileModel.objects.get(pk=user_id)
    context = {'user': profile_user}
    return render(request, 'learning_app/profile.html', context)

def like(request, mem_id):
    memory = Memory.objects.get(pk= mem_id)
    memory.likes +=1
    memory.save()
    messages.success(request, 'You liked a memory')
    return HttpResponseRedirect(reverse('index'))

def mail(request):
    name = request.POST.get('name')
    email_to = request.POST.get('email_to')
    email_from = request.POST.get('email_from')
    msg = request.POST.get('msg')
    print(name, email_to,email_from )

    send_mail('Feedback from '+name,msg,email_from,[email_to])
    return HttpResponseRedirect(reverse('index'))

def forum(request):
    if request.method == 'POST':
        user = request.POST.get('sent_by')
        text = request.POST.get('msgText')

        forum = Forum(user=user, text=text)
        forum.save()

    forum_posts = Forum.objects.all()
    context = {'forum_posts':forum_posts}

    return render(request, 'learning_app/forum.html', context)

def info(request):
    return render(request, 'learning_app/docs.html')
