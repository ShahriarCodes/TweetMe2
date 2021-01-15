from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tweet/<int:tweet_id>', views.tweet_detail_view, name='tweet-detail-view'),
    path('tweets/', views.tweet_list_view, name='tweet-list-view'),
]
