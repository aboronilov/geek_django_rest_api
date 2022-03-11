"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reviews.views import ActorAPIView, BiographyAPIView, HeroAPIView, CinemaAPIView, ReviewAPIView, ActorViewSet
from user.views import UserAPIView

router = DefaultRouter()
router.register(r'users', UserAPIView)
router.register(r'actors', ActorViewSet),
router.register(r'biography', BiographyAPIView),
router.register(r'hero', HeroAPIView),
router.register(r'cinema', CinemaAPIView)
router.register(r'review', ReviewAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
