from django.contrib import admin

from django.urls import path, include


from applications.music.views import MusicListView


urlpatterns = [
    path('music-list/', MusicListView.as_view()),
]
