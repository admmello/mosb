from rest_framework.viewsets import ModelViewSet

from mosb.training.models import Training
from .serializers import TrainingSerializer


class TrainingViewSet(ModelViewSet):
    serializer_class = TrainingSerializer

    def get_queryset(self):
        return Training.objects.all()

