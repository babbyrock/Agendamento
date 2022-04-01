from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, mixins, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from consulta.models import Consulta
from consulta.serializer import ConsultaSerializer
from user.permissions import EhSuperUser

class ConsultaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
   ):
    # permission_classes = (IsAuthenticated, )
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
