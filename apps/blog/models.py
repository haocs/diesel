from django.contrib.auth.models import User
from django.db import models

# Post
# Tag
# Tag_Post
# Comment

class PostManager(models.Manager):
    def create_post(self, title):
        post = self.create()
        return post

class Post(models.Model):
    PRIVACY_OPTS = (
        ('all', 'public'),
        ('myself', 'youself'),
    )

    STATUSES = (
        ('d', 'draft'),
        ('p', 'published'),
    )

    # Defin Post schema
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    last_modify_date = models.DateField()
    privacy = models.CharField(max_length=10, choices=PRIVACY_OPTS, default=PRIVACY_OPTS[0][0], blank=True)
    deleted = models.BooleanField(default=False, blank=True)
    deleted_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUSES[0][0], blank=True)

    objects = PostManager()



