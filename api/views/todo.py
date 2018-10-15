from rest_framework import viewsets

from ..serializers import TodoModelSerializer
from todo.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    authentication_classes = []
    permission_classes = []
