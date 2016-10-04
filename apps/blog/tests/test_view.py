from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from apps.blog.views import list_posts 

class PostTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_post_create_should_pass(self):
        pass

    def test_post_update(self):
        pass

    def test_post_delete(self):
        pass

class PostsTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_list_posts_should_pass(self):
        pass

