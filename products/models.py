from django.db import models

class Condition(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class BodySystem(models.Model):
    SYSTEM_CHOICES = [
        ('Nervous & Emotional', 'Nervous & Emotional'),
        ('Respiratory', 'Respiratory'),
        ('Digestive', 'Digestive'),
        ('Cardiovascular', 'Cardiovascular'),
        ('Urinary', 'Urinary'),
        ('Endocrine and Reproductive', 'Endocrine and Reproductive'),
        ('Lymphatic/Imune', 'Lymphatic/Imune'),
        ('Skin and connective tissues', 'Skin and connective tissues'),
        ('Muscles, bones, ligaments', 'Muscles, bones, ligaments'),
    ]
    name = models.CharField(max_length=255, choices=SYSTEM_CHOICES)
    
    def __str__(self):
            return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=200)
    condition = models.ManyToManyField(Condition)
    body_systems = models.ManyToManyField(BodySystem)
    image = models.ImageField(
        upload_to='images/', default='../product_default_putkpj', blank=True
    )
    
    def __str__(self):
        return self.name
    
