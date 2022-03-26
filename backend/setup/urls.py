from django.contrib import admin
from django.urls import include, path
from agendamento.views import EspecialidadesViewSet, MedicoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('especialidades', EspecialidadesViewSet, basename = 'Especialidades')
router.register('medicos', MedicoViewSet, basename = 'Medicos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
