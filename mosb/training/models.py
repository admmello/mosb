from django.db import models
from django.contrib.auth.models import User


class Training(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuário', related_name='userTraining')
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='instrutorTraining',
                                   related_name='instructor')
    initialDate = models.DateField(verbose_name='Data inicial', auto_now_add=True)
    validUntil = models.DateField(verbose_name='Validade', null=True, blank=True)

    class Meta:
        verbose_name = 'treino'
        verbose_name_plural = 'treinos'
        ordering = ('person__first_name', 'initialDate')

    def __str__(self):
        return self.person.username + ' - ' + str(self.initialDate)


class Workout(models.Model):
    MUSCLE_GROUP = (
        ('biceps', 'Bíceps'),
        ('triceps', 'Tríceps'),
        ('back', 'Costas'),
        ('chest', 'Peito'),
        ('quadriceps', 'Quadríceps'),
        ('posterior', 'Posterior'),
        ('shoulders', 'Ombro'),
    )

    name = models.CharField(max_length=150, verbose_name='nome')
    description = models.TextField(max_length=500, verbose_name='descrição', blank=True, null=True)
    muscleGroup = models.CharField(verbose_name='grupo muscular', choices=MUSCLE_GROUP, max_length=10)
    media = models.CharField(verbose_name='link video', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'exercício'
        verbose_name_plural = 'exercícios'

    def __str__(self):
        return self.name


class ItemTraining(models.Model):
    GROUP = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )

    training = models.ForeignKey(Training, verbose_name='treino', on_delete=models.CASCADE)
    sequence = models.IntegerField(verbose_name='sequencia', default=0)
    group = models.CharField(verbose_name='grupo', choices=GROUP, max_length=1, default='A')
    workout = models.ForeignKey(Workout, verbose_name='exercício', on_delete=models.PROTECT)
    repetition = models.CharField(verbose_name='repetições', max_length=20, blank=True, null=True)
    rounds = models.CharField(verbose_name='series', max_length=5, blank=True, null=True)
    rest = models.CharField(verbose_name='descanço', max_length=20, blank=True, null=True)
    cadence = models.CharField(verbose_name='cadencia', max_length=20, blank=True, null=True)
    observation = models.TextField(verbose_name='observação', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'item do treino'
        verbose_name_plural = 'itens do treino'
        ordering = ('group', 'sequence')

    def __str__(self):
        return self.group + ' - ' + self.workout.name