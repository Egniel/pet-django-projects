from rest_framework import viewsets

from api.serializers.resume import ResumeModelSerializer
from users.models import Resume


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer
