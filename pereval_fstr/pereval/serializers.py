from rest_framework import serializers

from pereval.models import Pereval


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'
