from rest_framework import serializers

from users.models import Resume


class ResumeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
