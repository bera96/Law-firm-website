from django.urls import path
from main.views import *

app_name = 'main'


urlpatterns = [
    path('', home_view, name='home'),
    path('contact-us', contact_view, name="contact"),
    path('faqs', questions_view, name="faqs"),
    path('about-us', aboutus_view, name="aboutus"),
    path('practice-areas', practice_areas_view, name="practice_areas"),

  
]