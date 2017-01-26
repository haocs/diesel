from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from apps.blog.models import Article, Tag


class ArticleTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_create_article_should_pass(self):
        now = timezone.now()
        article1 = Article(author=self.test_user, title='test article 1', content='test content 1', status='p',
                     created_timestamp=now)
        article1.save()
        article_get = Article.objects.latest('id')
        self.assertEqual(article1.title, article_get.title)
        self.assertEqual(article1.content, article_get.content)
        self.assertEqual(article1.status, article_get.status)
        self.assertEqual(article1.author.username, article_get.author.username)
        self.assertEqual('en', article_get.language)
        self.assertEqual('p', article_get.status)
        self.assertEqual('all', article_get.privacy)

    def test_create_article_with_tags_should_pass(self):
        now = timezone.now()
        article1 = Article(author=self.test_user, title='test article 1', content='test content 1', created_timestamp=now)
        article1.save()
        tag1 = Tag(name='testtag1')
        tag1.save()
        tag2 = Tag(name='testtag2')
        tag2.save()
        article1.tags.add(tag1, tag2)
        article_get = Article.objects.latest('id')
        self.assertEqual(article1.title, article_get.title)
        self.assertEqual(len(article_get.tags.all()), 2)
