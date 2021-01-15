from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tweet/<int:tweet_id>', views.tweet_detail_view, name='detail-view'),
]
