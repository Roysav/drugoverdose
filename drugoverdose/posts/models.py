import enum
import uuid

from django.conf import settings
from django.db import models


class PostType(models.TextChoices):
    QUESTION = 'question', 'Question'
    ANSWER = 'answer', 'Answer'


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=PostType.choices)
    title = models.CharField(max_length=200, null=True, default=None)
    body = models.TextField(null=True, default=None)
    parent = models.ForeignKey('Post', related_name='children', on_delete=models.CASCADE, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.SET_NULL, null=True)


