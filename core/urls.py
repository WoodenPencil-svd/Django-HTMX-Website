"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from a_posts.views import *
from django.conf import settings
from django.conf.urls.static import static
from a_users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home'),
    path('accounts/', include('allauth.urls')),
    path('post/create', post_create_view,name='post-create'),
    path('post/delete/<pk>/', post_delete_view,name='post-delete'),
    path('post/edit/<pk>/', post_edit_view,name='post-edit'),
    path('post/<pk>/', post_page_view,name='post-view'),
    path('category/<tag>',home_view, name= 'category'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name ='profile-edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

