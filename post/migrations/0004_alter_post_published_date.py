# Generated by Django 3.2.5 on 2021-08-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(auto_now_add=True, verbose_name='Publish Date'),
        ),
    ]
