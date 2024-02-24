from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Follower
from followers.serializers import FollowerSerializer


class FollowerAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='password123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_follower_list(self):
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_follower(self):
        another_user = User.objects.create_user(username='anotheruser',
                                                password='password123')
        data = {'followed': another_user.pk}
        response = self.client.post('/followers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_follower(self):
        another_user = User.objects.create_user(username='anotheruser',
                                                password='password123')
        follower = Follower.objects.create(owner=self.user, followed=another_user)
        response = self.client.delete(f'/followers/{follower.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
