from decimal import Decimal
from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Burger", price=Decimal("9.99"), inventory=10)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)