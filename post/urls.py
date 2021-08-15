from django.urls import path
from post.views import *


app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('<slug:slug>/detail/', post_detail, name='detail'),
    path('number-of-like',calculate_number_likes, name='number-of-like'),
  
]