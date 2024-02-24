from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Like
from posts.models import Post
from .serializers import LikeSerializer


class LikeSerializerTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='admin',
                                             password='1234')
        self.post = Post.objects.create(title='Test Post',
                                        description='This is a test post',
                                        owner=self.user)

    def test_like_serializer(self):

        request = self.factory.post('/likes/', {'post': self.post.pk})
        request.user = self.user
        serializer = LikeSerializer(
            data={'post': self.post.pk}, context={'request': request})
        self.assertTrue(serializer.is_valid())

        # Test to prevent user liking a post more than once
        Like.objects.create(owner=self.user, post=self.post)
        serializer = LikeSerializer(
            data={'post': self.post.pk}, context={'request': request})
        self.assertFalse(serializer.is_valid())
        self.assertIn('You have already liked the post.',
                      serializer.errors['non_field_errors'])
