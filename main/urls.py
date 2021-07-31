from django.urls import path
from main.views import *

app_name = 'main'


urlpatterns = [
    path('', home_view, name='home'),
    path('contact', contact_view, name="contact"),

  
]