from django.test import TestCase

from pereval.models import Users, Images, Coords


class UsersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Users.objects.create(first_name='Василий', last_name='Васильев', patronymic='Васильевич',
                             email='email@email.com', phone='+70123456789')

    def test_first_name_label(self):
        user = Users.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_last_name_label(self):
        user = Users.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Фамилия')

    def test_patronymic_label(self):
        user = Users.objects.get(id=1)
        field_label = user._meta.get_field('patronymic').verbose_name
        self.assertEquals(field_label, 'Отчество')

    def test_first_name_max_length(self):
        user = Users.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 15)

    def test_last_name_max_length(self):
        user = Users.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 20)

    def test_patronymic_max_length(self):
        user = Users.objects.get(id=1)
        max_length = user._meta.get_field('patronymic').max_length
        self.assertEquals(max_length, 20)

    def test_email_field_label(self):
        user = Users.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Электронная почта')

    def test_email_max_length(self):
        user = Users.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 30)

    def test_phone_field_label(self):
        user = Users.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Телефон')

    def test_phone_max_length(self):
        user = Users.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEquals(max_length, 12)

    def test_str(self):
        user = Users.objects.get(id=1)
        self.assertEquals(str(user), user.last_name + ' ' + user.first_name + ' ' +
                          user.patronymic + ' ' + user.email + ' ' + user.phone)


class ImagesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Images.objects.create(title_1='Название фото 1', image_1='Фотография 1', title_2='Название фото 2',
                              image_2='Фотография 2', title_3='Название фото 3', image_3='Фотография 3', )

    def test_title_1_field_label(self):
        title_1 = Images.objects.get(id=1)
        field_label = title_1._meta.get_field('title_1').verbose_name
        self.assertEquals(field_label, 'Название фото 1')

    def test_title_2_field_label(self):
        title_2 = Images.objects.get(id=1)
        field_label = title_2._meta.get_field('title_2').verbose_name
        self.assertEquals(field_label, 'Название фото 2')

    def test_title_3_field_label(self):
        title_3 = Images.objects.get(id=1)
        field_label = title_3._meta.get_field('title_3').verbose_name
        self.assertEquals(field_label, 'Название фото 3')

    def test_title_1_max_length(self):
        title_1 = Images.objects.get(id=1)
        max_length = title_1._meta.get_field('title_1').max_length
        self.assertEquals(max_length, 255)

    def test_title_2_max_length(self):
        title_2 = Images.objects.get(id=1)
        max_length = title_2._meta.get_field('title_2').max_length
        self.assertEquals(max_length, 255)

    def test_title_3_max_length(self):
        title_3 = Images.objects.get(id=1)
        max_length = title_3._meta.get_field('title_3').max_length
        self.assertEquals(max_length, 255)

    def test_image_1_field_label(self):
        image_1 = Images.objects.get(id=1)
        field_label = image_1._meta.get_field('image_1').verbose_name
        self.assertEquals(field_label, 'Фотография 1')

    def test_image_2_field_label(self):
        image_2 = Images.objects.get(id=1)
        field_label = image_2._meta.get_field('image_2').verbose_name
        self.assertEquals(field_label, 'Фотография 2')

    def test_image_3_field_label(self):
        image_3 = Images.objects.get(id=1)
        field_label = image_3._meta.get_field('image_3').verbose_name
        self.assertEquals(field_label, 'Фотография 3')

    def test_image_1_max_length(self):
        image_1 = Images.objects.get(id=1)
        max_length = image_1._meta.get_field('image_1').max_length
        self.assertEquals(max_length, 255)

    def test_image_2_max_length(self):
        image_2 = Images.objects.get(id=1)
        max_length = image_2._meta.get_field('image_2').max_length
        self.assertEquals(max_length, 255)

    def test_image_3_max_length(self):
        image_3 = Images.objects.get(id=1)
        max_length = image_3._meta.get_field('image_3').max_length
        self.assertEquals(max_length, 255)

    def test_str(self):
        image = Images.objects.get(id=1)
        self.assertEquals(str(image), image.title_1 + ' ' + image.title_2 + ' ' + image.title_3)


class CoordsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coords.objects.create(latitude=1.0, longitude=2.0, height=3)

    def test_latitude_field_label(self):
        coord = Coords.objects.create()
        field_label = coord._meta.get_field('latitude').verbose_name
        self.assertEquals(field_label, 'Широта')

    def test_longitude_field_label(self):
        coord = Coords.objects.create()
        field_label = coord._meta.get_field('longitude').verbose_name
        self.assertEquals(field_label, 'Долгота')

    def test_height_field_label(self):
        coord = Coords.objects.create()
        field_label = coord._meta.get_field('height').verbose_name
        self.assertEquals(field_label, 'Высота')

    def test_str(self):
        coord = Coords.objects.get(id=1)
        self.assertEquals(str(coord), f'{coord.latitude} {coord.longitude} {coord.height}')
