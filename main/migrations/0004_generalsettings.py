# Generated by Django 3.2.5 on 2021-08-14 10:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_description'),
        ('main', '0003_alter_faqs_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo')),
                ('number', models.CharField(max_length=120, verbose_name='Telefon')),
                ('address', models.CharField(max_length=255, verbose_name='Adres')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Email')),
                ('about', ckeditor.fields.RichTextField(verbose_name='AboutUs')),
                ('certificates', models.ManyToManyField(to='employee.Certificate', verbose_name="Office's Certificates")),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
    ]