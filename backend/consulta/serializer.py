from datetime import datetime
import json
from rest_framework import serializers
from agendamento.serializer import AgendaSerializer, EspecialidadeSerializer, MedicoSerializer
from consulta.models import Consulta
from agendamento.models import Agenda
from user.models import Usuario

class ConsultaSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        default=serializers.CurrentUserDefault()
    )
    agenda = serializers.SlugRelatedField(queryset=Agenda.objects.all(), slug_field='id', write_only=True)
    dia = serializers.ReadOnlyField(source='agenda.dia')
    medico = MedicoSerializer(source='agenda.medico', read_only=True)

    class Meta:
        model = Consulta
        fields = ['id','dia', 'horario', 'data_agendamento', 'medico', 'agenda', 'user']
        read_only_field = ['user']
        # extra_kwargs = {
        #     'validate_date': {'read_only': False},
        # }

    def __init__(self, *args, **kwargs):
        super(ConsultaSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 4