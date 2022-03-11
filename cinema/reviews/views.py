from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .models import Actor, Biography, Hero, Cinema, Review
from .serializers import ActorSerializer, BiographySerializer, HeroSerializer, CinemaSerializer, ReviewSerializer


class ActorAPIView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_queryset(self):
        if self.request.query_params:
            year = self.request.query_params['year'][0]
            return Actor.objects.filter(birthday_year__gte=year)
        else:
            return Actor.objects.all()


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filterset_fields = ['name', 'birthday_year']


class BiographyAPIView(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class HeroAPIView(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class CinemaLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class CinemaAPIView(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    pagination_class = CinemaLimitOffsetPagination


class ReviewAPIView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




