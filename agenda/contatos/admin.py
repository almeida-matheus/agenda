from django.contrib import admin
from .models import Categoria, Contato

# * na sessão /admin/contatos/contato irá mostrar:
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostrar')
    # * id, nome e sobrenome se torna clicavel pra editar
    list_display_links = ('id', 'nome', 'sobrenome')
    # * adicionar filtro por nome e sobrenome
    # list_filter = ('nome', 'sobrenome')#
    # * exibir 10 elementos por página
    list_per_page = 10
    # * campo pra pesquisar tal coluna
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
