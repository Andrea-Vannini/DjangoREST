from django.contrib.auth.models import User, Group

from rest_framework import serializers

from unit.models import Symbol, Unit, System


class SymbolSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Symbol
		fields = ('pk', 'symbol',)


class SymbolDetailSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	
	class Meta:
		model = Symbol
		fields = ('pk', 'symbol', 'author',)


class UnitSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Unit
		fields = ('pk', 'name', )


class UnitDetailSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	symbol = SymbolSerializer(many=False, read_only=True)

	class Meta:
		model = Unit
		fields = ('pk', 'name', 'symbol', 'author',)


class SystemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = System
		fields = ('pk', 'name',)


class SystemDetailSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	units = UnitSerializer(many=True, read_only=True)

	class Meta:
		model = System
		fields = ('pk', 'name', 'units', 'author',)
