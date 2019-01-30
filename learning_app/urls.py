from django.conf.urls import url
from learning_app import views

app_name = 'learning_app'

urlpatterns = [
    url(r'^register/$', views.register, name = "register"),
    url(r'^login/$', views.user_login, name = 'user_login')
]
