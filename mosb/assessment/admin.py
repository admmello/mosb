from django.contrib import admin
from .models import Skinfold, Antropometria, Anamnese, AnamneseQuestion, PostureQuestion, Posture, Assessment


class SkinfoldInLine(admin.StackedInline):
    model = Skinfold
    extra = 0
    fields = (('subescapular', 'abdomen', 'coxaMedial',),
              ('triceps', 'peitoral','axiliarMedia', 'supraIliaca',),)


class AntropometriaInLine(admin.StackedInline):
    model = Antropometria
    extra = 0
    fields = (('bloodPressure', 'oximetria', 'fcRest'),
              ('size', 'weight'),
              ('chest', 'waist', 'abdomen', 'hip'),
              ('leftArm', 'leftForearm', 'leftContractedArm', 'leftThigh', 'leftCalf'),
              ('rightArm', 'rightForearm', 'rightContractedArm', 'rightThigh', 'rightCalf'),
              'fist',)


class AnamneseInLine(admin.StackedInline):
    model = Anamnese
    extra = 0
    fields = (('question', 'answer'),)


class PostureInLine(admin.StackedInline):
    model = Posture
    extra = 0


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [SkinfoldInLine, AntropometriaInLine, AnamneseInLine, PostureInLine]
    fields = (('person', 'instructor',), ('photoFront', 'photoRight', 'photoLeft', 'photoBack'),)
    


# admin.site.register(Skinfold)
# admin.site.register(Antropometria)
# admin.site.register(Posture)
admin.site.register(AnamneseQuestion)
admin.site.register(PostureQuestion)
admin.site.register(Assessment, AssessmentAdmin)

