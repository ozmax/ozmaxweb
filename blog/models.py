from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nickname


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = RichTextUploadingField()
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']