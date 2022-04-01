from django.urls import path
from rest_framework import routers

from agendamento.models import Agenda
from consulta.views import ConsultaViewSet
from .views import (
    EspecialidadesViewSet,
    MedicoViewSet,
    HorarioViewSet,
    AgendaViewSet
)


