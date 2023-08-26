import enum
import uuid

from django.db import models


class PostType(models.Choices):
    QUESTION = enum.auto()
    ANSWER = enum.auto()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=PostType)
    title = models.CharField(max_length=200, null=True, default=None)
    body = models.TextField(null=True, default=None)
    parent = models.ForeignKey('Post', related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)

