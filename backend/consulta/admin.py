from django.contrib import admin

from consulta.models import Consulta

class Consultas(admin.ModelAdmin):
    list_display = ('id', 'horario')
    list_display_links = ('id',)
    list_per_page = 20

admin.site.register(Consulta, Consultas)
