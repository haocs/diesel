from django.test import TestCase
from django.contrib.auth.models import User

from apps.blog.models import Post, Tag


class CreateTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_post_create(self):
        pass

    def test_post_update(self):
        pass

    def test_post_delete(self):
        pass
