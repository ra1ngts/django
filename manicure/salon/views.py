from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from salon.models import User
from salon.serializers import UserRecordsSerializer


class UserRecords(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRecordsSerializer
    http_method_names = ['get', 'post', 'delete', 'head', 'options']
    permission_classes = [IsAuthenticated]
