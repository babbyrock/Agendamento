from django.db import models

from agendamento.models import Agenda, Horario, Medico

class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='agenda_id')
    horario = models.CharField(max_length=30, null=True)
    # horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True,null=True, related_name='agenda_medico')

    