from rest_framework import generics

from pereval.models import Pereval
from pereval.serializers import PerevalSerializer


class PerevalAPI(generics.ListCreateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
