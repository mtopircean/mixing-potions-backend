# Generated by Django 3.2.23 on 2024-02-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(
                default='../apprentice_vcpdlr', upload_to='images/'),
        ),
    ]