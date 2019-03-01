from django.conf.urls import url
from learning_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'learning_app'

urlpatterns = [
    url(r'^register/$', views.register, name = "register"),
    url(r'^login/$', views.user_login, name = 'user_login'),
        url(r'^feed/$', views.feed, name = 'feed'),

    url(r'feed/add', views.add, name = 'add'),
    url(r'users/', views.list_users, name = 'list_users'),
    url('like/(?P<mem_id>\d+)', views.like, name='like'),
    url('profile/(?P<user_id>\d+)', views.view_profile, name='view_profile'),
    url('profile/mail', views.mail, name='mail'),
    url(r'feed/delete/(?P<note_id>\d+)', views.delete_note, name = 'delete_note'),
    url(r'^forum/$', views.forum, name = 'forum'),
    url(r'^info/$', views.info, name = 'info'),








]
