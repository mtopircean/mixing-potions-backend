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
        response - self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_follower(self):
        data = {'follower': self.user.pk}
        response = self.client.post('/followers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)

    def test_delete_follower(self):
        follower = Follower.objects.create(owner=self.user, follower=self.user)
        response = self.client.delete(f'/followers/{follower.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)
