from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Symbol(models.Model):
	symbol = models.CharField(max_length=5, unique=True, verbose_name='symbol')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	class Meta:
		verbose_name_plural = 'Symbols'

	def __str__(self):
		return self.symbol


class Unit(models.Model):
	name = models.CharField(max_length=20, unique=True, verbose_name='name')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE, default=1)

	class Meta:
		verbose_name_plural = 'Units'

	def __str__(self):
		return self.name


class System(models.Model):
	name = models.CharField(max_length=20, unique=True, verbose_name='name')
	units = models.ManyToManyField(Unit, blank=True, related_name="systemsforunit", verbose_name='units')
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	class Meta:
		verbose_name_plural = 'Systems'

	def __str__(self):
		return self.name
