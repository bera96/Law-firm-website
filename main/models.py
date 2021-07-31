from django.db import models
from django.db.models.fields import CharField







class Message(models.Model):
    name = models.CharField(max_length=120, verbose_name="Ad")
    phone_number =models.CharField(max_length=120, verbose_name="Telefon")
    email = models.EmailField(max_length=254, default=None, verbose_name="Email")
    subject = models.TextField(verbose_name="Mesaj")
    date = models.DateTimeField(auto_now_add=True)


