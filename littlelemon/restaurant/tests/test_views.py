from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.menu_item = Menu.objects.create(title="Pizza", price=10.99, inventory=15)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
