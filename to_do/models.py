from django.db import models

# Create your models here.


class Tarefa(models.Model):
    realizado = models.BooleanField(null=False)
    descricao = models.CharField(max_length=50, null=False, blank=False)
    data = models.DateTimeField()

    def __str__(self):
        return f'Tarefa [nome={self.descricao}]'
