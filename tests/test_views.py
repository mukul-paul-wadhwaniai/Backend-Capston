from django.test import TestCase
from rest_framework import status
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def test_add_menu_item(self):
        data = {'title': 'test-item', 'price': '1', 'inventory': '1'}
        url = 'http://127.0.0.1:8000/restaurant/menu'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.last().title, 'test-item')
        self.assertEqual(Menu.objects.last().price, 1)
        self.assertEqual(Menu.objects.last().inventory, 1)