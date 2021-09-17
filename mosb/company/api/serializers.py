from rest_framework.serializers import ModelSerializer

from mosb.company.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'cnpj', 'name', 'address', 'logo',)
