from rest_framework import serializers

from accessory.models import Accessory
from brides.models import Bride
from dress.models import Dress


class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = '__all__'


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'


class BrideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bride
        fields = '__all__'
