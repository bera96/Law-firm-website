from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField





class Post(models.Model):

    title = models.CharField(max_length=255, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    published_date = models.DateTimeField(verbose_name="Publish Date",auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    number_like = models.IntegerField(editable=False, default=0)
    number_share = models.IntegerField(editable=False, default=0)
    slug = models.SlugField(unique=True, editable=False, max_length=265)



    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)



    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})


    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    

    class Meta:
        ordering = ['-published_date', 'id']