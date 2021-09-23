"""
views.py
"""
from rest_framework import viewsets

from .serializers import HeroSerializer, CreatorSerializer, SuperpowersSerializer
from .models import Hero, Creator, Superpowers


class HeroViewSet(viewsets.ModelViewSet): #ModelViewSet handles GET and POST
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all().order_by('name')
    serializer_class = CreatorSerializer

class SuperpowersViewSet(viewsets.ModelViewSet):
    queryset = Superpowers.objects.all().order_by('name')
    serializer_class = SuperpowersSerializer
