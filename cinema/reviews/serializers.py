from rest_framework import serializers

from user.serializers import UserSerializer, SimpleUserSerializer
from .models import Actor, Biography, Hero, Cinema, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ['id']


class BiographySerializer(serializers.ModelSerializer):
    actor = ActorSerializer()

    class Meta:
        model = Biography
        exclude = ['id']


class HeroSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()

    class Meta:
        model = Hero
        exclude = ['id']


class CinemaSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cinema
        exclude = ['id']


class SimpleCinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['name']


class ReviewSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()
    cinema = SimpleCinemaSerializer()

    class Meta:
        model = Review
        exclude = ['id']


