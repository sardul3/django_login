"""learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from learning_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$', views.index, name = "index"),
    url(r'^$', views.info, name = "info"),

    url(r'^learning_app/', include('learning_app.urls')),
    url(r'^logout/$', views.user_logout, name = 'user_logout'),
    url(r'^feed/$', views.feed, name = 'feed')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
