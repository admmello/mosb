from django.contrib import admin
from .models import Training, Workout, ItemTraining
from django.forms import TextInput, Textarea
from django.db import models


class ItemTrainingInLine(admin.StackedInline):
    # reformat tamanho dos campo no django admin
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 60})},
    }
    fields = (('group', 'workout',), ('sequence', 'rounds', 'repetition',),
                                      ('rest', 'cadence'), 'observation')
    # raw_id_fields = ('workout',)
    model = ItemTraining
    extra = 0


class TrainingAdmin(admin.ModelAdmin):
    fields = (('user', 'instructor', 'validUntil',),)
    # raw_id_fields = ('user',)
    # search_fields = ('user__username', 'user__first_name', 'title',)
    inlines = [ItemTrainingInLine]


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscleGroup', 'media',)
    search_fields = ('name', 'muscleGroup',)
    list_filter = ('muscleGroup',)
    fields = ('muscleGroup', 'name', 'media', 'description',)


admin.site.register(Training, TrainingAdmin)
admin.site.register(Workout, WorkoutAdmin)
# admin.site.register(ItemTraining)
