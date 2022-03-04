from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Actor, Biography, Hero, Cinema, Review
from .serializers import ActorSerializer, BiographySerializer, HeroSerializer, CinemaSerializer, ReviewSerializer


class ActorAPIView(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class BiographyAPIView(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class HeroAPIView(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class CinemaAPIView(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ReviewAPIView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



