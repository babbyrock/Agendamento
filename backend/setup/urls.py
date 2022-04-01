from django.contrib import admin
from django.urls import include, path
from agendamento.views import AgendaViewSet, EspecialidadesViewSet, HorarioViewSet, MedicoViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from consulta.views import ConsultaViewSet
from user.views import ListaUsuarios, UsuariosViewSet


router = routers.DefaultRouter()
router.register('especialidades', EspecialidadesViewSet, basename = 'Especialidades')
router.register('medicos', MedicoViewSet, basename = 'Medicos')
router.register('horarios', HorarioViewSet, basename = 'Horários')
router.register('agendas', AgendaViewSet, basename = 'Agendas')
router.register('cadastrar_usuario', UsuariosViewSet, basename='Cadastrar Usuário')
router.register('consultas', ConsultaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('cadastrar_usuario/', ListaUsuarios.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('auth/', include('rest_framework.urls')),
]
