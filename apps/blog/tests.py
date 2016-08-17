from django.test import TestCase

from .models import Post


class PostTestCase(TestCase):

    def test_create_post(self):
        post1 = Post(title='test post 1', content='test content 1', status='p')
        post1.save()
        post_get = Post.objects.latest('id')
        self.assertEqual(post1.title, post_get.title)