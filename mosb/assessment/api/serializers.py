from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User

from mosb.assessment.models import Assessment, Skinfold, Antropometria, Anamnese, AnamneseQuestion
from mosb.assessment.models import Posture, PostureQuestion


class PersonSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class SkinfoldSerializer(ModelSerializer):
    class Meta:
        model = Skinfold
        exclude = ('assessment',)


class AntropometriaSerializer(ModelSerializer):
    class Meta:
        model = Antropometria
        exclude = ('assessment',)


class AnamneseQuestionSerializer(ModelSerializer):
    groupDescription = SerializerMethodField()

    class Meta:
        model = AnamneseQuestion
        fields = ('id', 'group', 'groupDescription', 'question')

    def get_groupDescription(self, obj):
        return obj.get_group_display()


class AnamneseSerializer(ModelSerializer):
    question = AnamneseQuestionSerializer()

    class Meta:
        model = Anamnese
        fields = ('id', 'question', 'answer',)


class PostureQuestionSerializer(ModelSerializer):
    groupDescription = SerializerMethodField()

    class Meta:
        model = PostureQuestion
        fields = ('id', 'group', 'groupDescription', 'question')

    def get_groupDescription(self, obj):
        return obj.get_group_display()


class PostureSerializer(ModelSerializer):
    question = PostureQuestionSerializer()

    class Meta:
        model = Posture
        fields = ('id', 'question', 'answer',)


class AssessmentSerializer(ModelSerializer):
    person = PersonSerializer()
    instructor = PersonSerializer()
    skinfold = SkinfoldSerializer()
    antropometria = AntropometriaSerializer()
    anamneses = AnamneseSerializer(source='anamnese_set', many=True)
    postures = AnamneseSerializer(source='posture_set', many=True)

    class Meta:
        model = Assessment
        fields = ('id', 'person', 'instructor', 'date', 'photoFront', 'photoBack', 'photoRight', 'photoLeft',
                  'skinfold', 'antropometria', 'anamneses', 'postures',)
