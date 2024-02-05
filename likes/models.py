from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can only like a post once.
        unique_together = ['owner', 'post']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner} likes {self.post}"
