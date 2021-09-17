from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from mosb.company.models import Company
from .serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('cnpj', 'name',)
    filter_fields = ('cnpj', 'name',)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Company.objects.all()

