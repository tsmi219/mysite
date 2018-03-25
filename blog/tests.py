from django.test import TestCase
from django.test import Client
from django.urls import reverse

class CreatePostTestCase(TestCase):

    def test_blog_not_authenicated(self):
        client = Client()
        client.logout()
        url = reverse('post_new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        #self.assertRedirects(response, "/accounts/login", status_code=302)
