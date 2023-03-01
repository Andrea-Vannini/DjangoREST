from django.contrib.auth.models import User, Group

from rest_framework import serializers

from unit.models import Symbol, Unit, System

from source.models import Origin, Source


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


class OriginSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Origin
		fields = ('pk', 'name', )


class OriginDetailSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Origin
		fields = ('pk', 'name', 'url',)


class SourceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Source
		fields = ('pk', 'name', )


class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
	origin = OriginSerializer(many=False, read_only=True)

	class Meta:
		model = Source
		fields = ('pk', 'name', 'origin', 'url',)
