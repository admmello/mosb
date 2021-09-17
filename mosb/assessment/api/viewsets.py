from rest_framework.viewsets import ModelViewSet

from mosb.assessment.models import Assessment
from .serializers import AssessmentSerializer


class AssessmentViewSet(ModelViewSet):
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        return Assessment.objects.all()
