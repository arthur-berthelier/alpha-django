from django.test import TestCase



# Create your tests here.




from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/') # notre homepage
        self.assertEqual(response.status_code, 200) #200 = OK

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)








