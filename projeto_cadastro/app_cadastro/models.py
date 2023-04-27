from django.db import models

class Cadastro(models.Model):
    id_produto = models.AutoField(primary_key=True)
    produto = models.TextField(max_length=255)
    valor = models.FloatField()
    quantidade = models.IntegerField()
