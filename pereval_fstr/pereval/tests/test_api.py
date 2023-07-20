from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pereval.models import Pereval, Coords, Users, Images
from pereval.serializers import PerevalSerializer


class SubmitDataPostTest(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(beauty_title='Пер.', title='Заголовок 1', other_titles='Заголовок 2',
                                                connect='Соединяет', add_time='2023-07-20 16:30:32.859243+00',
                                                status='new',
                                                coordinates=Coords.objects.create(latitude=1.0, longitude=2.0,
                                                                                  height=3),
                                                user=Users.objects.create(first_name='Имя', last_name='Фамилия',
                                                                          patronymic='Отчество',
                                                                          email='email@email.com'),
                                                images=Images.objects.create(title_1='title_1', image_1='image_1'))
        self.pereval_2 = Pereval.objects.create(beauty_title='Пер.', title='Заголовок 1', other_titles='Заголовок 2',
                                                connect='Соединяет', add_time='2023-07-20 16:30:32.859243+00',
                                                status='new',
                                                coordinates=Coords.objects.create(latitude=1.0, longitude=2.0,
                                                                                  height=3),
                                                user=Users.objects.create(first_name='Имя', last_name='Фамилия',
                                                                          patronymic='Отчество',
                                                                          email='email@email.com'),
                                                images=Images.objects.create(title_1='title_1', image_1='image_1'))

    def test_get_list(self):
        url = reverse('submitData')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEquals(dict(serializer_data), response.json())
        self.assertEquals(len(serializer_data), 2)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
