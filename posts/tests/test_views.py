

from rest_framework.test import APITestCase
from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from django.urls import reverse

from rest_framework import status

class TestPostViewSet(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            'admin',
            first_name='Janusz',
            last_name='Testowy'
        )

        self.post = Post.objects.create(
            title='testowy post',
            content='testowa zawartosc posta mememem',
            author=self.admin,
        )

    def test_posts_list(self):

        url = reverse('post-list')
        response = self.client.get(url, format='json')
        #print(response.status_code)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(True,False)