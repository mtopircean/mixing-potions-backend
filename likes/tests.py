from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Like
from posts.models import Post
from .serializers import LikeSerializer


class LikeSerializerTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin',
                                             password='1234')
        self.post = Post.objects.create(title='Test Post',
                                        content='This is a test post',
                                        owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_like_serializer(self):
        data = {'post': self.post.pk}
        serializer = LikeSerializer(
            data=data, context={'request': self.client})
        self.assertTrue(serializer.is_valid())

        # Test to prevent user liking a post more then once
        Like.objects.create(owner=self.user, post=self.post)
        serializer = LikeSerializer(
            data=data, context={'request': self.client})
        self.assertFalse(serializer.is_valid())
        self.assertIn('You have already liked the post.',
                      serializer.errors['non_field_errors'])
