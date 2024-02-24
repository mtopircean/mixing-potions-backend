from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin',
                                             password='1234')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Post',
                                        description='This is a post',
                                        owner=self.user)

    def test_retrieve_post(self):
        response = self.client.get(f'/posts/{self.post.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        new_title = 'New Post Title'
        response = self.client.patch(f'/posts/{self.post.pk}/',
                                     {'title': new_title})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, new_title)
