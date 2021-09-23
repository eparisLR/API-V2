"""
Serialize models to JSON
"""
from rest_framework import serializers

from .models import Hero
from .models import Creator
from .models import Superpowers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias','superpowers',)

class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creator
        fields = ('id','name',)

class SuperpowersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Superpowers
        fields = ('id','name',)
