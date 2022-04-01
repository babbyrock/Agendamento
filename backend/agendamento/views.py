from rest_framework import viewsets, mixins, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from agendamento.models import Agenda, Especialidade, Horario, Medico
from agendamento.serializer import AgendaSerializer, EspecialidadeSerializer, HorarioSerializer, MedicoSerializer
from user.permissions import EhSuperUser
from django_filters.rest_framework import DjangoFilterBackend




class EspecialidadesViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Especialidade.objects.all()  
    serializer_class = EspecialidadeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']

class MedicoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filter_fields = ('especialidade',)
   
class HorarioViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class AgendaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class AgendaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

