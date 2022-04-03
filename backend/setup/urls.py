from django.contrib import admin
from django.urls import include, path
# from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from agendamento.views import AgendaViewSet, CreateAgendaViewSet, EspecialidadesViewSet, HorarioViewSet, MedicoViewSet
from rest_framework import routers, views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
from consulta.views import ConsultaViewSet
from user.views import ListaUsuarios, UsuariosViewSet


router = routers.DefaultRouter()
router.register('especialidades', EspecialidadesViewSet, basename = 'Especialidades')
router.register('medicos', MedicoViewSet, basename = 'Medicos')
router.register('horarios', HorarioViewSet, basename = 'Horários')
router.register('agendas', AgendaViewSet, basename = 'Agendas')
router.register('criar_agendas', CreateAgendaViewSet, basename = 'Criar Agendas')
router.register('cadastrar_usuario', UsuariosViewSet, basename='Cadastrar Usuário')
router.register('consultas', ConsultaViewSet, basename = 'Consultas')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]

