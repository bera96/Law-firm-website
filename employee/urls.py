from django.urls import path
from employee.views import *


app_name = 'employee'

urlpatterns = [
    path('<slug:slug>/detail/', employee_detail, name='detail'),
  
]