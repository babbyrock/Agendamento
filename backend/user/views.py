from user.permissions import EhSuperUser
from user.serializer import UsuarioSerializer
from .models import Usuario
from rest_framework import viewsets, generics


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    EhSuperUser

class ListaUsuarios(generics.ListAPIView):
    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer

