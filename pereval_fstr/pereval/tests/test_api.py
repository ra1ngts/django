from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pereval.models import Pereval, Coords, Users, Images
from pereval.serializers import PerevalSerializer


class SubmitDataTest(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(beauty_title='Пер.',
                                                title='Перевал Pas de Chevres',
                                                other_titles='Па де Шевр',
                                                connect='ледник Шейлон (glacier de Cheilon) - поселок Аролла',
                                                add_time='2023-07-20 16:30:32.859243+00',
                                                status='new',
                                                level='winter-1A',
                                                coordinates=Coords.objects.create(latitude=1.0,
                                                                                  longitude=2.0,
                                                                                  height=3),
                                                user=Users.objects.create(first_name='Михаил',
                                                                          last_name='Михайлов',
                                                                          patronymic='Михайлович',
                                                                          email='misha50@example.com',
                                                                          phone='+70123456789'),
                                                images=Images.objects.create(title_1='Перевал Pas de Chevres-1',
                                                                             image_1='https://upload.wikimedia.org/wikipedia/commons/0/0f/Panorama_Ost_Pas_de_Ch%C3%A8vres.jpg',
                                                                             title_2='',
                                                                             image_2='',
                                                                             title_3='',
                                                                             image_3=''))
        self.pereval_2 = Pereval.objects.create(beauty_title='Пер.',
                                                title='Перевал Teodulpass',
                                                other_titles='Теодуль, Teodulo',
                                                connect='ледник Теодуль и долину реки Мармор',
                                                add_time='2023-07-20 16:30:32.859243+00',
                                                status='new',
                                                level='winter-1A',
                                                coordinates=Coords.objects.create(latitude=1.0,
                                                                                  longitude=2.0,
                                                                                  height=3),
                                                user=Users.objects.create(first_name='Василий',
                                                                          last_name='Васильев',
                                                                          patronymic='Васильевич',
                                                                          email='vasyl60@example.com',
                                                                          phone='+70123456789'),
                                                images=Images.objects.create(title_1='Перевал Teodulpass-1',
                                                                             image_1='https://upload.wikimedia.org/wikipedia/commons/e/ef/Colle_del_Teodulo_001.jpg',
                                                                             title_2='Перевал Teodulpass-2',
                                                                             image_2='https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Rif-theodulo.jpg/800px-Rif-theodulo.jpg',
                                                                             title_3='',
                                                                             image_3=''))

    def test_get_submitData_list(self):
        url = reverse('submitData')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEquals(serializer_data, response.data['results'], msg='Ошибка')
        self.assertEquals(len(serializer_data), 2, msg='Ошибка')
        self.assertEquals(status.HTTP_200_OK, response.status_code, msg='Ошибка')
