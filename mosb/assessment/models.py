from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Assessment(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuário', related_name='userAssessment')
    instructor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='instrutor', related_name='instructorAssessment')
    date = models.DateField(auto_now_add=True)
    photoFront = models.ImageField(verbose_name='foto frontal', upload_to='userPhotos', blank=True, null=True)
    photoRight = models.ImageField(verbose_name='foto direita', upload_to='userPhotos', blank=True, null=True)
    photoLeft = models.ImageField(verbose_name='foto esquerda', upload_to='userPhotos', blank=True, null=True)
    photoBack = models.ImageField(verbose_name='foto costas', upload_to='userPhotos', blank=True, null=True)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    def __str__(self):
        return 'Avaliação %s - %s' %(self.id, self.person.username)


class Skinfold(models.Model):
    # PROTOCOLS = (
    #     ('3DC', 'Jackson, Pollock e Col (3DC)'),
    #     ('7DC', 'Jackson, Pollock e Col (7DC)'),
    #     ('PNF', 'Pernoe, Nelson e Fischer'),
    #     ('WET', 'Wetman e Col'),
    #     ('GUE', 'Guedes'),
    #     ('FAU', 'Faulkner'),
    # )

    assessment = models.OneToOneField(Assessment, on_delete=models.CASCADE, verbose_name='avaliação')
    subescapular = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    triceps = models.DecimalField(verbose_name='tríceps', max_digits=5, decimal_places=2, blank=True, null=True)
    peitoral = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    axiliarMedia = models.DecimalField(verbose_name='axiliar media', max_digits=5, decimal_places=2, blank=True,
                                       null=True)
    supraIliaca = models.DecimalField(verbose_name='supra ilíaca', max_digits=5, decimal_places=2, blank=True,
                                      null=True)
    abdomen = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    coxaMedial = models.DecimalField(verbose_name='coxa medial', max_digits=5, decimal_places=2, blank=True, null=True)
    # protocol = models.CharField(verbose_name='protocolo', choices=PROTOCOLS, max_length=3, blank=True, null=True,
    #                             default='3DC')

    class Meta:
        verbose_name = 'dobra cutânea'
        verbose_name_plural = 'dobras cutâneas'

    def __str__(self):
        return 'Retornar % de gordura'


class Antropometria(models.Model):
    assessment = models.OneToOneField(Assessment, on_delete=models.CASCADE, verbose_name='avaliação')
    bloodPressure = models.CharField('pressao sanguinea', max_length=10, blank=True, null=True)
    oximetria = models.IntegerField(validators=(MinValueValidator(0),), blank=True, null=True)
    fcRest = models.IntegerField(verbose_name='FC Repouso', validators=(MinValueValidator(0),), blank=True, null=True)
    size = models.DecimalField(verbose_name='altura', max_digits=3, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(verbose_name='peso', max_digits=5, decimal_places=2, blank=True, null=True)
    chest = models.DecimalField(verbose_name='peitoral', max_digits=5, decimal_places=2, blank=True, null=True)
    waist = models.DecimalField(verbose_name='cintura', max_digits=5, decimal_places=2, blank=True, null=True)
    abdomen = models.DecimalField(verbose_name='abdômen', max_digits=5, decimal_places=2, blank=True, null=True)
    hip = models.DecimalField(verbose_name='quadril', max_digits=5, decimal_places=2, blank=True, null=True)
    leftArm = models.DecimalField(verbose_name='braço esquerdo', max_digits=5, decimal_places=2, blank=True, null=True)
    leftForearm = models.DecimalField(verbose_name='antebraço esquerdo', max_digits=5, decimal_places=2, blank=True, null=True)
    leftContractedArm = models.DecimalField(verbose_name='braço esquerdo contraído', max_digits=5, decimal_places=2, blank=True, null=True)
    leftThigh = models.DecimalField(verbose_name='Coxa esquerda', max_digits=5, decimal_places=2, blank=True, null=True)
    leftCalf = models.DecimalField(verbose_name='Panturrilha esquerda', max_digits=5, decimal_places=2, blank=True, null=True)
    rightArm = models.DecimalField(verbose_name='braço direito', max_digits=5, decimal_places=2, blank=True, null=True)
    rightForearm = models.DecimalField(verbose_name='antebraço direito', max_digits=5, decimal_places=2, blank=True, null=True)
    rightContractedArm = models.DecimalField(verbose_name='braço direito contraído', max_digits=5, decimal_places=2, blank=True, null=True)
    rightThigh = models.DecimalField(verbose_name='Coxa direita', max_digits=5, decimal_places=2, blank=True, null=True)
    rightCalf = models.DecimalField(verbose_name='Panturrilha direita', max_digits=5, decimal_places=2, blank=True, null=True)
    fist = models.DecimalField(verbose_name='Punho', max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'antropometria'
        verbose_name_plural = 'antropometrias'

    def __str__(self):
        return 'Retornar IMC'


class AnamneseQuestion(models.Model):
    GROUPS = (
        ('PQ', 'PAR-Q'),
        ('HM', 'Histórico médico'),
        ('SD', 'Sintomas de doenças'),
        ('EV', 'estilo de vida'),
        ('EE', 'Expectativa de exercício'),
        ('IC', 'Auto imagem corporal'),
        ('IP', 'IPAQ'),
    )

    group = models.CharField(verbose_name='grupo', choices=GROUPS, max_length=2)
    question = models.CharField(verbose_name='perguntas', max_length=1000)

    class Meta:
        verbose_name = 'questão anamnese'
        verbose_name_plural = 'questões anamnese'

    def __str__(self):
        return '%s - %s' % (self.get_group_display(), self.question)


class Anamnese(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, verbose_name='avaliação')
    question = models.ForeignKey(AnamneseQuestion, on_delete=models.CASCADE, verbose_name='questao')
    answer = models.CharField(verbose_name='resposta', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'anamnese'
        verbose_name_plural = 'anamneses'

    def __str__(self):
        return 'Anamnese'


class PostureQuestion(models.Model):
    GROUPS = (
        ('F', 'Frontal'),
        ('P', 'Posterior'),
        ('L', 'Lateral'),
    )

    group = models.CharField(verbose_name='grupo', choices=GROUPS, max_length=1)
    question = models.CharField(verbose_name='questão', max_length=100)

    class Meta:
        verbose_name = 'Questão postural'
        verbose_name_plural = 'Questões posturais'

    def __str__(self):
        return '%s - %s' % (self.get_group_display(), self.question)


class Posture(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, verbose_name='avaliação')
    question = models.ForeignKey(PostureQuestion, on_delete=models.CASCADE, verbose_name='questão')
    answer = models.CharField(verbose_name='resposta', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Postural'
        verbose_name_plural = 'Posturais'

    def __str__(self):
        return 'Avaliação postural'







