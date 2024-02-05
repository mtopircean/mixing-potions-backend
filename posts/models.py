from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from profiles.models import Profile


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, blank=True)

    image = models.ImageField(
        upload_to='images/', default='../default_post_image_vf1akc', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    def get_owner_nickname(self):
        profile = Profile.objects.filter(owner=self.owner).first()
        return profile.nickname if profile else None
