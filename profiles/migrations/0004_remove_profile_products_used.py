# Generated by Django 3.2.23 on 2024-02-05 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_products_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='products_used',
        ),
    ]
