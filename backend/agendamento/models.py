from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=30)
    crm = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome