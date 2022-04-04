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

    def get_queryset(self):
        user = self.request.user
        # print(Consulta.objects.all())
        if user.is_anonymous:
            return Consulta.objects.all()
        return Consulta.objects.filter(user=user)

    
