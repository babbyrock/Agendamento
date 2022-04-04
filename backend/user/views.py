from urllib import response
from user.permissions import EhSuperUser
from user.serializer import LoginSerializer, UsuarioSerializer
from .models import Usuario
from rest_framework import viewsets, generics, permissions
from django.contrib.auth import authenticate
from rest_framework import response, status



class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    EhSuperUser

class ListaUsuarios(generics.ListAPIView):
    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer

class LoginAPIView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = LoginSerializer
    
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer=self.serializer_class(user)
            
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': "Credenciais inválidas, tente de novo"}, status=status.HTTP_400_BAD_REQUEST)

class AuthUserAPIView(generics.GenericAPIView):
    permissions_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        user = request.user

        serializer = UsuarioSerializer(user)

        return response.Response({'user':serializer.data})

