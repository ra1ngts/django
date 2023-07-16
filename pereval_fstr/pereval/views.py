from rest_framework import mixins, generics

from pereval.models import Pereval
from pereval.serializers import PerevalSerializer, PerevalDetailSerializer


class SubmitData(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SubmitDataDetail(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
