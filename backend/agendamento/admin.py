from django.contrib import admin
from agendamento.models import Especialidade, Medico

class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Especialidade, Especialidades)


class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'email', 'telefone', 'especialidade')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Medico, Medicos)
