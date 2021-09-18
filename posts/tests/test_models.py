from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            'admin',
            first_name= 'Janusz',
            last_name= 'Testowy'
        )

        self.post = Post.objects.create(
            title='testowy post',
            content='testowa zawartosc posta mememem',
            author=self.admin,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), 'testowy post (Janusz Testowy)')
    # python manage.py test

