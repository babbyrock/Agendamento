from django.contrib import admin
from agendamento.models import Agenda, Especialidade, Horario, Medico

class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Especialidade, Especialidades)


class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'email', 'telefone')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Medico, Medicos)

class Horarios(admin.ModelAdmin):
    list_display = ('id', 'hora')
    list_display_links = ('id','hora')
    search_fields = ('hora',)
    list_per_page = 20

admin.site.register(Horario, Horarios)


admin.site.register(Agenda)