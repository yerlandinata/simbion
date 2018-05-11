from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SimbionFrontEndTest(TestCase):

    def test_get_landing_page(self):
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, 200)
