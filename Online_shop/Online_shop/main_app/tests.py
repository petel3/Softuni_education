from django.test import TestCase

from Online_shop.accounts.models import ShopUser
from Online_shop.main_app.models import Flower, Jewelry, Plant, Souvenir


class URLTests(TestCase):

    def test_indexpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_flowerspage(self):
        response = self.client.get('/flowers/')
        self.assertEqual(response.status_code, 200)

    def test_create_flowerspage(self):
        response = self.client.get('/flowers/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_flowerspage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Flower.objects.create(name='Rose', quantity='3', type='Basket'
                              , description='Beautiful rose', price='15.23', user_key_id=1)

        response = self.client.get('/flowers/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_flowerspage(self):
        response = self.client.get('/flowers/details/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_flowerspage(self):
        response = self.client.get('/flowers/details/1')
        self.assertEqual(response.status_code, 302)
        delete_response = self.client.get('/flowers/delete/1')
        self.assertEqual(delete_response.status_code, 404)

    def test_jewelrypage(self):
        response = self.client.get('/jewelry/')
        self.assertEqual(response.status_code, 200)

    def test_create_jewelrypage(self):
        response = self.client.get('/jewelry/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_jewelrypage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Jewelry.objects.create(name='Necklace', quantity='3', materials='Silver'
                               , description='Beautiful Necklace', price='5.23', user_key_id=2)
        response = self.client.get('/jewelry/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_jewelrypage(self):
        response = self.client.get('/jewelry/details/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_jewelrypage(self):
        response = self.client.get('/jewelry/details/1')
        self.assertEqual(response.status_code, 302)
        delete_response = self.client.get('/jewelry/delete/1')
        self.assertEqual(delete_response.status_code, 404)

    def test_plantspage(self):
        response = self.client.get('/plants/')
        self.assertEqual(response.status_code, 200)

    def test_create_plantspage(self):
        response = self.client.get('/plants/create/')
        self.assertEqual(response.status_code, 200)

    def test_edit_plantspage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Plant.objects.create(name='Kala', quantity='5', type='Winter plant'
                             , description='Beautiful Necklace', price='5.23', user_key_id=3)
        response = self.client.get('/plants/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_plantspage(self):
        response = self.client.get('/plants/details/1')
        self.assertEqual(response.status_code, 404)

    def test_delete_plantspage(self):
        delete_response = self.client.get('/plants/delete/1')
        self.assertEqual(delete_response.status_code, 404)

    def test_souvenirspage(self):
        response = self.client.get('/souvenirs/')
        self.assertEqual(response.status_code, 200)

    def test_create_souvenirspage(self):
        response = self.client.get('/souvenirs/create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_souvenirspage(self):
        ShopUser.objects.create(username='django1', password='Valkyrie123', is_staff=1, is_superuser=1)
        Souvenir.objects.create(name='Glass', quantity='2', type='Normal'
                                , description='Beautiful Glass', price='35.23', user_key_id=4)
        response = self.client.get('/souvenirs/edit/1')
        self.assertEqual(response.status_code, 200)

    def test_details_souvenirspage(self):
        response = self.client.get('/souvenirs/details/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_souvenirspage(self):
        delete_response = self.client.get('/souvenirs/delete/1')
        self.assertEqual(delete_response.status_code, 404)

    def test_offerspage(self):
        response = self.client.get('/quotations/')
        self.assertEqual(response.status_code, 200)
