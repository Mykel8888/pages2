from django.test import  SimpleTestCase,TestCase

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code, 200)

class AboutPageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code, 200)



class BasePageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response=self.client.get('/base/')
        self.assertEqual(response.status_code, 200)

