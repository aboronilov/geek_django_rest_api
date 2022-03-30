from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory
from reviews.models import Actor, Biography
from user.models import User
from user.views import UserAPIView


class TestCinemaApi(APITestCase):
    def setUp(self):
        self.users_url = '/api/users/'
        self.actors_url = '/api/actors/'
        self.cinema_url = '/api/cinema/'
        self.biography_url = '/api/biography/'

    def test_get_all_users(self):
        factory = APIRequestFactory()
        request = factory.get(self.users_url)
        view = UserAPIView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_actor(self):
        actor = Actor.objects.create(name="Мэтью Макконахи", birthday_year=1969)
        client = APIClient()
        response = client.get(f'{self.actors_url}{actor.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_cinema(self):
        response = self.client.get(self.cinema_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_biography_fail_without_auth(self):
        biography = mixer.blend(Biography)
        path = f'{self.biography_url}{biography.id}/'
        data = {'text': 'Отличный актер', 'actor': 'Мэтью Макконахи'}
        response = self.client.put(path=path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
