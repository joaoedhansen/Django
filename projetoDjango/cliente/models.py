from django.db import models

class Cliente(models.Model):
    nome = models.CharField(
        u"Nome",
        max_length=30
    )
    ativo = models.BooleanField(
        default=True
    )
    obs = models.CharField(
        u"Observação",
        max_length=100
    )
    numero_ficha = models.IntegerField(
        default=0
    )
