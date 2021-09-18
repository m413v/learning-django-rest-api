

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from django.urls import reverse

from rest_framework import status

from posts.views import PostViewSet


class TestPostViewSet(APITestCase):
    url = reverse('post-list')

    def setUp(self):
        self.admin = User.objects.create_superuser(
            'admin',
            first_name='Janusz',
            last_name='Testowy'
        )

        self.user = User.objects.create_user(
            'user',
            first_name='User',
            last_name='Zwykly'
        )

        self.post = Post.objects.create(
            title='testowy post',
            content='testowa zawartosc posta mememem',
            author=self.admin,
        )

    def test_posts_list(self):
        response = self.client.get(self.url, format='json')
        #print(response.status_code)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(True,False)

    def test_standard_user_cannot_create_post(self):

        request = APIRequestFactory().post(self.url, data={})
        force_authenticate(request, user=self.user)
        create_post = PostViewSet.as_view({'post':'create'})
        response = create_post(request)
        print(response.status_code)
        # self.assertEqual(True,False)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

