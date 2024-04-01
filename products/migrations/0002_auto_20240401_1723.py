# Generated by Django 3.2.23 on 2024-04-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodysystem',
            name='name',
            field=models.CharField(choices=[('Nervous & Emotional', 'Nervous & Emotional'), ('Respiratory', 'Respiratory'), ('Digestive', 'Digestive'), ('Cardiovascular', 'Cardiovascular'), ('Urinary', 'Urinary'), ('Endocrine and Reproductive', 'Endocrine and Reproductive'), ('Lymphatic/Imune', 'Lymphatic/Imune'), ('Skin and connective tissues', 'Skin and connective tissues'), ('Muscles, bones, ligaments', 'Muscles, bones, ligaments')], max_length=500),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
