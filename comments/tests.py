from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer


class CommentAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_comment_list(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        post = Post.objects.create(
            title='Test Post', description='Test description', owner=self.user)
        data = {'comment_text': 'Test Comment', 'post': post.pk}
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_comment(self):
        post = Post.objects.create(
            title='Test Post', description='Test description', owner=self.user)
        comment = Comment.objects.create(
            owner=self.user, comment_text='Test Comment', post=post)
        response = self.client.delete(f'/comments/{comment.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
