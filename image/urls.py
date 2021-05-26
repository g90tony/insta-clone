from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('upload/', views.upload, name='Upload'),
    path('profile/', views.profile, name='Profile'),
    path('profile/create', views.create_profile, name='Create Profile'),
    path('profile/view/<int:user_id>/', views.view_profile, name='View Profile'),
    path('post/view/<int:post_id>/', views.view, name='View Post'),
    path('profile/view/search', views.search, name='Search'),
]