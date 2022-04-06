import graphene
import requests
from graphene_django import DjangoObjectType

from reviews.models import Cinema, Actor


class CinemaType(DjangoObjectType):
    class Meta:
        model = Cinema
        fields = '__all__'


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = '__all__'


class Query(graphene.ObjectType):
    all_cinema = graphene.List(CinemaType)
    all_actors = graphene.List(ActorType)
    cinema_by_actor_name = graphene.List(CinemaType, name=graphene.String(required=False))

    def resolve_all_cinema(root, info):
        return Cinema.objects.all()

    def resolve_all_actors(root, info):
        return Actor.objects.all()

    def resolve_cinema_by_name(root, info, name=None):
        cinema = Cinema.objects.all()
        if name:
            cinema = cinema.filter(name=name)
        return cinema


schema = graphene.Schema(query=Query)
