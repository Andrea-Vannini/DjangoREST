from django.contrib.auth.models import User, Group
from rest_framework import serializers
from unit.models import Unit


class UnitSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Unit
		fields = ('pk', 'name', 'author',)

class UnitDetailSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Unit
		fields = ('pk', 'name', 'author',)
