from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from apps.blog.views import list_articles 

class ArticleTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_article_create_should_pass(self):
        pass

    def test_article_update(self):
        pass

    def test_article_delete(self):
        pass

class ArticlesTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_list_articles_should_pass(self):
        pass

