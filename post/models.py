from django.db import models
from django.urls import reverse




class Post(models.Model):

    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    published_date = models.DateTimeField(verbose_name="Publish Date")




    def __str__(self):
        return self.title



    
    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"id": self.id})
    