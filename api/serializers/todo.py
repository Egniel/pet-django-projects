from rest_framework import serializers

from todo.models import Todo


class TodoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('text', 'done')
