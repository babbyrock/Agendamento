from rest_framework import viewsets
from agendamento.models import Especialidade, Medico
from agendamento.serializer import EspecialidadeSerializer, MedicoSerializer

class EspecialidadesViewSet(viewsets.ModelViewSet):
    """Exibindo todos de especialidade"""
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    """Exibindo todos de especialidade"""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

