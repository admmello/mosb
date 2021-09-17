from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User

from mosb.training.models import Training, ItemTraining, Workout


class PersonSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class WorkoutSerializer(ModelSerializer):
    muscleGroupDescription = SerializerMethodField()

    class Meta:
        model = Workout
        fields = ('id', 'name', 'muscleGroup', 'muscleGroupDescription', 'media')

    def get_muscleGroupDescription(self, obj):
        return obj.get_muscleGroup_display()


class ItemTrainingSerializer(ModelSerializer):
    workout = WorkoutSerializer()

    class Meta:
        model = ItemTraining
        # depth = 1
        fields = ('id', 'sequence', 'group', 'workout', 'repetition',
                  'rounds', 'rest', 'cadence', 'observation',)


class TrainingSerializer(ModelSerializer):
    person = PersonSerializer()
    instructor = PersonSerializer()
    workouts = ItemTrainingSerializer(source='itemtraining_set', many=True)

    class Meta:
        model = Training
        fields = ('id', 'person', 'instructor', 'initialDate', 'validUntil', 'workouts')
