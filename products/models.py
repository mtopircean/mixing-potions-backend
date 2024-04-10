from django.db import models


class Condition(models.Model):
    """
    Represents a health condition that a product can address.
    """
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class BodySystem(models.Model):
    """
    Represents the body system that a product targets or is related to.
    Defines a list of choices for the body system a product can target.
    """
    SYSTEM_CHOICES = [
        ('Nervous & Emotional', 'Nervous & Emotional'),
        ('Respiratory', 'Respiratory'),
        ('Digestive', 'Digestive'),
        ('Cardiovascular', 'Cardiovascular'),
        ('Urinary', 'Urinary'),
        ('Endocrine and Reproductive', 'Endocrine and Reproductive'),
        ('Lymphatic/Immune', 'Lymphatic/Immune'),
        ('Skin and connective tissues', 'Skin and connective tissues'),
        ('Muscles, bones, ligaments', 'Muscles, bones, ligaments'),
    ]
    name = models.CharField(max_length=500, choices=SYSTEM_CHOICES)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents a product, which can be associated
    with multiple conditions and body systems.
    """
    name = models.CharField(max_length=200)
    condition = models.ManyToManyField(Condition)
    body_systems = models.ManyToManyField(BodySystem)
    image = models.ImageField(
        upload_to='images/', default='../product_default_putkpj', blank=True
    )

    def __str__(self):
        return self.name
