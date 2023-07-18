from rest_framework import mixins, generics, status, filters
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from pereval.models import Pereval
from pereval.serializers import PerevalSerializer, PerevalDetailSerializer


class SubmitData(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__email']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({f'status': status.HTTP_201_CREATED, 'message': 'Запись успешно создана', 'id': obj.id})
        if status.HTTP_400_BAD_REQUEST:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': serializer.errors})
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': serializer.errors})


class SubmitDetailData(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalDetailSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Статус данных изменился на: {instance.status}. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PerevalDetailSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Статус данных изменился на: {instance.status}. Редактирование запрещено')
            serializer.save()
            return Response({'state': 1, 'message': 'Данные успешно отредактированы'})
        return Response({'state': 0, 'message': serializer.errors})
