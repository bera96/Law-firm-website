from django.db import models
from django.db.models.fields import CharField







class Message(models.Model):
    name = models.CharField(max_length=120)
    phone_number =models.CharField(max_length=120)
    email = models.EmailField(max_length=254, default=None)
    subject = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


