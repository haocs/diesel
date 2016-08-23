from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User

from apps.blog.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username='testuser', email='test@diesel', password='testPasswd'
        )

    def test_create_post_should_pass(self):
        post1 = Post(author=self.test_user, title='test post 1', content='test content 1', status='p')
        post1.save()
        post_get = Post.objects.latest('id')
        self.assertEqual(post1.title, post_get.title)
        self.assertEqual(post1.content, post_get.content)
        self.assertEqual(post1.status, post_get.status)
        self.assertEqual(post1.author.username, post_get.author.username)

    def test_create_post_with_tags_should_pass(self):
        pass

    def test_create_tag_should_pass(self):
        pass
