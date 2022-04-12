from django.urls import path

from apps.accounts.api import views


app_name = 'accounts'

urlpatterns = [
    path('', views.UserListAPI.as_view(), name='user-list'),
]