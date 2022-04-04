from rest_framework.authentication import get_authorization_header, BaseAuthentication

from rest_framework import exceptions
import jwt

from django.conf import settings

from user.models import Usuario

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed('Token não é válido')

        token=auth_token[1]


        

        try:
            payload=jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            email=payload['email']
            print(email)

            user=Usuario.objects.get(email=email)

            print(Usuario.objects.all())


            return (user, token)
        
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('Token está expirado, faça o login novamente') 
        
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed('Token é inválido') 

        except Usuario.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed('Usuário não encontrado')

        

        return super().authenticate(request)
