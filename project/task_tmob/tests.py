from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from .models import Redirect

from factory import django
import factory
from factory.faker import faker

fake = faker.Faker()

class RedirectFactory(django.DjangoModelFactory):
    class Meta:
        model = Redirect

    key = fake.uri_page()
    url = fake.image_url()
    active = False


class RedirectViewsetTestCase(APITestCase):
    url = '/api/get_resource/'

    def setUp(self):
        self.client = APIClient()
        self.redirect = RedirectFactory.create()

    def test_reject_if_not_param(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "key not supplied")

    def test_reject_if_key_not_exist(self):
        response = self.client.get(f"{self.url}?key=KEY")

        self.assertEqual(response.status_code, 404)

    def test_reject_if_key_is_not_active(self):
        response = self.client.get(f"{self.url}?key={self.redirect.key}")

        self.assertEqual(response.status_code, 404)

    def test_success_if_key_is_active(self):
        obj = Redirect.objects.get(key=self.redirect.key)
        obj.active = True
        obj.save()
        response = self.client.get(f"{self.url}?key={self.redirect.key}")
        self.assertEqual(response.status_code, 200)







