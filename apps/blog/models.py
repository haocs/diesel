from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Post
# Tag
# Tag_Post
# Comment


class Post(models.Model):
    PRIVACY_OPTS = (
        ('all', 'public'),
        ('myself', 'yourself'),
    )

    STATUSES = (
        ('d', 'draft'),
        ('p', 'published'),
    )

    LANGUAGES = (
        ('cn', 'chinese'),
        ('en', 'english'),
    )

    # Define Post schema
    language = models.CharField(max_length=5, choices=LANGUAGES, default=LANGUAGES[0][0], blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField(default='', blank=True)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    mod_timestamp = models.DateField(default=datetime.now, blank=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY_OPTS, default=PRIVACY_OPTS[0][0], blank=True)
    deleted = models.BooleanField(default=False, blank=True)
    del_timestamp = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUSES[0][0], blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
