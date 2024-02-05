from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.test import APIClient
from rest_framework import status
        
class ProfileAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='johndoe', password='abcd')
        self.profile = Profile.objects.get(owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile(self):
        """
        Test retrieving a profile
        """
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner'], self.user.username)
        
    def test_update_profile(self):
        """
        Test updating a profile
        """
        new_nickname = 'newnickname'
        response = self.client.patch(f'/profiles/{self.profile.id}/', {'nickname': new_nickname})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.nickname, new_nickname)