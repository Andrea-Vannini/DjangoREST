from django.db import models
from django.contrib.auth.models import User


class Source(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name='name')
	url = models.URLField(max_length=200, unique=True, verbose_name='url')
	description = models.TextField(max_length=1000, blank=True, verbose_name='description')

	class Meta:
		verbose_name_plural = 'Sources'

	def __str__(self):
		return self.name
