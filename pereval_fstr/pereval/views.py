from rest_framework import mixins, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from pereval.models import Pereval
from pereval.serializers import PerevalSerializer, PerevalDetailSerializer


class SubmitData(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubmitDetailData(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError('Статус данных изменился. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError('Статус данных изменился. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})
