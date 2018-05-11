from django.test import TestCase

# Create your tests here.
class SimbionFrontEndTest(TestCase):

    def test_get_landing_page(self):
        r = self.client.get('/web/landing')
        self.assertEqual(r.status_code, 200)
