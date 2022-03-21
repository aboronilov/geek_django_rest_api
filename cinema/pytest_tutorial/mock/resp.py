import requests
import responses
from unittest.mock import MagicMock

# подмена реального запроса вовне
def get_data_from_wiki():
    response = requests.get('https://wikipedia.org')
    return response.text


@responses.activate
def test_wiki():
    responses.add(responses.GET, 'https://wikipedia.org', json={'status': 'OK'}, status=200)
    print(get_data_from_wiki())


test_wiki()

# подмена резлуьтата работы функции или метода класса
class A:
    def get_one(self):
        return 1

a = A()
a.get_one = MagicMock(return_value = 2)
print(a.get_one())