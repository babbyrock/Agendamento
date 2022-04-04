from asyncore import read, write
from rest_framework import serializers
from agendamento.models import Agenda, Especialidade, Horario, Medico
import time

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('id', 'nome')

class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(source="especialidade_id", read_only=True)
    especialidade_id = serializers.PrimaryKeyRelatedField(queryset=Especialidade.objects.all(), write_only=True)
    class Meta:
        model = Medico
        fields = (
            'id',
            'nome',
            'crm',
            'email',
            'telefone',
            'especialidade_id',
            'especialidade'
        )
    def __init__(self, *args, **kwargs):
        super(MedicoSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 3


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'hora']
    
    

class AgendaSerializer(serializers.ModelSerializer):
    horario = serializers.SlugRelatedField(many=True, queryset=Horario.objects.all(), slug_field='hora')
    class Meta:
        model = Agenda
        fields = ('id', 'medico', 'dia','horario')

    def __init__(self, *args, **kwargs):
        super(AgendaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2