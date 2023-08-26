import uuid

from django.db import models


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
