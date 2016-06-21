from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Post
# Tag
# Tag_Post
# Comment


class PostManager(models.Manager):
    def create_post(self, user_id, title, content, privacy, status, tags):
        post = self.create(user=user_id, title=title, content=content, privacy=privacy, status=status)
        if tags:
            # add new tags and update TagPost
            pass
        return post


class Post(models.Model):
    PRIVACY_OPTS = (
        ('all', 'public'),
        ('myself', 'yourself'),
    )

    STATUSES = (
        ('d', 'draft'),
        ('p', 'published'),
    )

    # Define Post schema
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField(default='', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    last_modify_date = models.DateField()
    privacy = models.CharField(max_length=10, choices=PRIVACY_OPTS, default=PRIVACY_OPTS[0][0], blank=True)
    deleted = models.BooleanField(default=False, blank=True)
    deleted_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUSES[0][0], blank=True)

    objects = PostManager()


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

