from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from apps.blog.models import Post, Tag


class PostTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_create_post_should_pass(self):
        now = timezone.now()
        post1 = Post(author=self.test_user, title='test post 1', content='test content 1', status='p',
                     created_timestamp=now)
        post1.save()
        post_get = Post.objects.latest('id')
        self.assertEqual(post1.title, post_get.title)
        self.assertEqual(post1.content, post_get.content)
        self.assertEqual(post1.status, post_get.status)
        self.assertEqual(post1.author.username, post_get.author.username)
        self.assertEqual('en', post_get.language)
        self.assertEqual('p', post_get.status)
        self.assertEqual('all', post_get.privacy)

    def test_create_post_with_tags_should_pass(self):
        now = timezone.now()
        post1 = Post(author=self.test_user, title='test post 1', content='test content 1', created_timestamp=now)
        post1.save()
        tag1 = Tag(name='testtag1')
        tag1.save()
        tag2 = Tag(name='testtag2')
        tag2.save()
        post1.tags.add(tag1, tag2)
        post_get = Post.objects.latest('id')
        self.assertEqual(post1.title, post_get.title)
        self.assertEqual(len(post_get.tags.all()), 2)