from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Unit(models.Model):
	name = models.CharField(max_length=20, unique=True, verbose_name='name')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	
	class Meta:
		verbose_name_plural = 'Units'

	def __str__(self):
		return self.name
