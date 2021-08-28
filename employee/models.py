from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Certificate(models.Model):

    title = models.CharField(verbose_name='Certificate Title', max_length = 255)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title




class UpperCaseField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseField,self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).title()



class PracticeAreas(models.Model):

    title = UpperCaseField(max_length = 255)
    desc = RichTextField(verbose_name="Desciption")
    slug = models.SlugField(unique=True, editable=False, max_length=265)



    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(PracticeAreas, self).save(*args, **kwargs)





    
    def get_absolute_url(self):
        return reverse("main:practice_areas", kwargs={"slug": self.slug})


    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Employee.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    class Meta:
        verbose_name_plural = "Practice Areas"



class Employee(models.Model):

    name = models.CharField(max_length=255, verbose_name="Name")
    surname = models.CharField(max_length=255, verbose_name="Surname")
    description = RichTextField(verbose_name="Description")
    faculty =  models.CharField(max_length=255, verbose_name="Faculty")
    graduated_date=models.DateField(verbose_name="Graduated Date")
    image = models.ImageField(null=True, blank=True, verbose_name="Employee's Photo")
    areas = models.ManyToManyField(PracticeAreas, verbose_name="Practice Areas")
    certificates = models.ManyToManyField(Certificate,  verbose_name="Employee's Certificates")
    slug = models.SlugField(unique=True, editable=False, max_length=265)



    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Employee, self).save(*args, **kwargs)



    def __str__(self):
        return self.name + self.surname

    
    def get_absolute_url(self):
        return reverse("employee:detail", kwargs={"slug": self.slug})


    def get_unique_slug(self):
        title = self.name + self.surname
        slug = slugify(title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Employee.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    




   