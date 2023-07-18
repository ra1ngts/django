from rest_framework import mixins, generics, status
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

    def post(self, request, format=None):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({f'status': status.HTTP_201_CREATED, 'message': 'Запись успешно создана', 'id': obj.id})
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})


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
                raise ValidationError(f'Статус данных изменился на: {instance.status}. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Статус данных изменился на: {instance.status}. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})
