# Generated by Django 3.2.23 on 2024-01-20 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_nickname_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='nickname_post',
        ),
    ]
