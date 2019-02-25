from django.conf.urls import url
from learning_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'learning_app'

urlpatterns = [
    url(r'^register/$', views.register, name = "register"),
    url(r'^login/$', views.user_login, name = 'user_login'),
    url(r'feed/add', views.add, name = 'add'),
    url(r'users/', views.list_users, name = 'list_users')



]
