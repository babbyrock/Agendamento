from django.db import models
import django_filters

class Especialidade(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=30)
    crm = models.CharField(unique=True,max_length=6)
    email = models.EmailField()
    telefone = models.CharField(max_length=30)
    especialidade_id = models.ForeignKey(Especialidade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Horario(models.Model):
    hora = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.hora

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.ManyToManyField(Horario, blank=True)


    # def __str__(self):
    #     return f'{self.medico}'
