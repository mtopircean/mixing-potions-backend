from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin',
                                             password='1234',
                                             is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Product')

    def test_retrieve_product(self):
        response = self.client.get(f'/products/{self.product.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        new_name = 'New Name'
        response = self.client.patch(f'/products/{self.product.pk}/',
                                     {'name': new_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, new_name)
