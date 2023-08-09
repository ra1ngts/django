from decouple import config
from django.core.mail import send_mail
from rest_framework import serializers

from salon.models import User, Salon, Services, Master


class UserRecordsSerializer(serializers.ModelSerializer):
    salon = serializers.SlugRelatedField(slug_field='title', queryset=Salon.objects.all(), label='Название салона')
    master = serializers.SlugRelatedField(slug_field='name', queryset=Master.objects.all(), label='Имя мастера')
    services = serializers.SlugRelatedField(slug_field='title', queryset=Services.objects.all(),
                                            label='Название услуги')

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(UserRecordsSerializer, self).to_representation(instance)
        representation['date'] = instance.date.strftime('%d.%m.%Y в %H:%M')
        return representation

    def create(self, validate_data):
        instance = super(UserRecordsSerializer, self).create(validate_data)
        send_mail(
            f'Приветствуем! Напоминаем о вашей записи на услугу: {instance.services} в нашем салоне красоты.',
            f'{instance.name}, ждем Вас {instance.date.strftime("%d.%m.%Y в %H:%M")} в салоне: {instance.salon}. Если у вас возникли изменения в планах или вам нужно перенести запись, пожалуйста, свяжитесь с нами по номеру: +70123456789. С нетерпением ждем встречи!',
            config('DEFAULT_FROM_EMAIL'),
            [config('DEFAULT_FROM_EMAIL')],
            fail_silently=False,
        )
        print('Новая запись на почте')
        return instance
