from django.urls import path

from apps.boards.api import views


app_name = 'boards'

urlpatterns = [
    path('', views.BoardListAPI.as_view(), name='board-list'),
]