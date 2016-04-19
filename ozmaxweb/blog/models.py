from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255)

class Author(models.Model):
		pass

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField()
	author = models.ForeignKey(Author)
	category = models.ForeignKey(Category)
	created_at = models.DateTimeField()
	modified_at = models.DateTimeField()

