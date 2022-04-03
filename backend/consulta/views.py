from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework import viewsets, mixins, permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from consulta.models import Consulta
from consulta.serializer import ConsultaSerializer
from user.permissions import EhSuperUser
from django.http import QueryDict
from rest_framework.viewsets import ModelViewSet

class ConsultaViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    # def list(self,request):
    #     # v =self.kwargs.get('horario', )
    #     # query = request.GET.get('horario')
    #     print(self)
    #     return Response(self.serializer_class(self.queryset, many=True).data,
    #                     status=status.HTTP_200_OK)
