from django.urls import path
from post.views import *


app_name = 'employee'

urlpatterns = [
    path('<slug:slug>/detail/', post_detail, name='detail'),
  
]