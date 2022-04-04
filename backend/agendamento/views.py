from rest_framework import viewsets, mixins, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from agendamento.models import Agenda, Especialidade, Horario, Medico
from agendamento.serializer import AgendaSerializer, EspecialidadeSerializer, HorarioSerializer, MedicoSerializer
from user.permissions import EhSuperUser
from django_filters.rest_framework import DjangoFilterBackend



class EspecialidadesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Especialidade.objects.all()  
    serializer_class = EspecialidadeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']

class CreateEspecialidadesViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Especialidade.objects.all()  
    serializer_class = EspecialidadeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']

class MedicoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filter_fields = ('especialidade_id',)

class CreateMedicoViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
   
class HorarioViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class CreateHorarioViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    )
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class CreateAgendaViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
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

