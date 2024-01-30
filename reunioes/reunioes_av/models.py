from django.db import models

class ReuniaoAv(models.Model):
    nome = models.CharField(max_length=120)
    titulo = models.CharField(max_length=20)
    descricao = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=100)
    dia = models.DateField()
    horario = models.TimeField()

def __str__(self):
    return self.name
