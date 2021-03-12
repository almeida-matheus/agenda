from django.db import models
from django.utils import timezone

#cria a tabela contatos_categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    # mudar a representação de objeto/classe
    # representar o objeto com o campo principal
    def __str__(self):
        return self.nome

#cria a tabela contatos_contato
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    #select para selecionar o nome das categorias e adicionar
    #quando uma categoria for deletada, oq vai fazer com os contatos dessa categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome

