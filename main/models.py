from django.db import models
from ckeditor.fields import RichTextField
from employee.models import UpperCaseField






class Message(models.Model):
    name = models.CharField(max_length=120, verbose_name="Ad")
    phone_number =models.CharField(max_length=120, verbose_name="Telefon")
    email = models.EmailField(max_length=254, default=None, verbose_name="Email")
    subject = models.TextField(verbose_name="Mesaj")
    date = models.DateTimeField(auto_now_add=True)




class Faqs(models.Model):
    title = UpperCaseField(max_length = 255)
    desc = RichTextField(verbose_name="Desciption")




    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Faqs"




