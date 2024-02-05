from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} on "{self.post}": "{self.comment_text[:60]}..."'
