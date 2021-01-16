from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path('', views.home_view, name='home'),

    path('create_tweet/', views.tweet_create_view,
         name='tweet-create-view'),

    path('tweet/<int:tweet_id>', views.tweet_detail_view,
         name='tweet-detail-view'),

    path('tweets/', views.tweet_list_view,
         name='tweet-list-view'),

]
