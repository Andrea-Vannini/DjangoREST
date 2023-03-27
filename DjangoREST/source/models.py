from django.db import models


class Origin(models.Model):
	name = models.CharField(max_length=100, unique=False, verbose_name='name')
	url = models.URLField(max_length=200, unique=False, verbose_name='url')

	class Meta:
		verbose_name_plural = 'Origins'

	def __str__(self):
		return self.name


class Source(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name='name')
	origin = models.ForeignKey(Origin, on_delete=models.CASCADE, default=1)
	url = models.URLField(max_length=400, unique=False, verbose_name='url')

	class Meta:
		verbose_name_plural = 'Sources'

	def __str__(self):
		return self.name
