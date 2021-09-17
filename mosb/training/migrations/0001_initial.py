# Generated by Django 3.2.7 on 2021-09-16 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nome')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='descrição')),
                ('muscleGroup', models.CharField(choices=[('biceps', 'Bíceps'), ('triceps', 'Tríceps'), ('back', 'Costas'), ('chest', 'Peito'), ('quadriceps', 'Quadríceps'), ('posterior', 'Posterior'), ('shoulders', 'Ombro')], max_length=10, verbose_name='grupo muscular')),
                ('media', models.CharField(blank=True, max_length=300, null=True, verbose_name='link video')),
            ],
            options={
                'verbose_name': 'exercício',
                'verbose_name_plural': 'exercícios',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initialDate', models.DateField(auto_now_add=True, verbose_name='Data inicial')),
                ('validUntil', models.DateField(blank=True, null=True, verbose_name='Validade')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instructor', to=settings.AUTH_USER_MODEL, verbose_name='instrutorTraining')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTraining', to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'treino',
                'verbose_name_plural': 'treinos',
                'ordering': ('user__first_name', 'initialDate'),
            },
        ),
        migrations.CreateModel(
            name='ItemTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(default=0, verbose_name='sequencia')),
                ('group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1, verbose_name='grupo')),
                ('repetition', models.CharField(blank=True, max_length=20, null=True, verbose_name='repetições')),
                ('rounds', models.CharField(blank=True, max_length=5, null=True, verbose_name='series')),
                ('rest', models.CharField(blank=True, max_length=20, null=True, verbose_name='descanço')),
                ('cadence', models.CharField(blank=True, max_length=20, null=True, verbose_name='cadencia')),
                ('observation', models.TextField(blank=True, max_length=200, null=True, verbose_name='observação')),
                ('traning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.training', verbose_name='treino')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training.workout', verbose_name='exercício')),
            ],
            options={
                'verbose_name': 'item do treino',
                'verbose_name_plural': 'itens do treino',
                'ordering': ('group', 'sequence'),
            },
        ),
    ]