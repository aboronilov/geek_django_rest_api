from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserAPIView(ModelViewSet):
    queryset = User.objects.all().order_by('uid')
    serializer_class = UserSerializer
