from django.db import models
from django.utils import timezone

LISTA_CATEGORIAS = (
    ("ANALISE", "Análise"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)


# Criar a Classe Filme
class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


# Criar a SubClasses Episodios

# Criar a Classe Usuario
