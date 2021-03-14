from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    # ? select * from Contato
    # contatos = Contato.objects.all()
    #* ordena pelo id por ordem decrescente
    #* filtrar todos os objetos se o mostrar = True
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    #* arquivo paginação
    paginator = Paginator(contatos, 20)
    # url/?p=<numero>
    page = request.GET.get('p')
    contatos = paginator.get_page(page)


    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    #obter um objeto onde id=contato_id
    # contato = Contato.objects.get(id=contato_id)
	# try:
	#     contato = Contato.objects.get(id=contato_id)
	# 	return render(request, 'contatos/ver_contato.html', {
    #     'contato': contato
    #     })
	# except Contato.DoesNotExist as e:
	# 	raise Http404()

    contato = get_object_or_404(Contato, id=contato_id)

    #* se o contato nao estiver visivel na tabela, nao tem como buscar ele no url/<id>
    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    #* obter o valor digitado url/?termo=<value> 
    # o input tem name="termo"
    termo = request.GET.get('termo')
    #busca por nome: (icontains => like)
    # contatos = Contato.objects.order_by('-id').filter(
    #     mostrar=True, nome__icontains=termo, sobrenome=__icontains=termo,
    # )
    # print(contatos.query)
    #? where mostrar = true AND nome like =%% AND sobrenome like=%%

    if termo is None or not termo:
        # raise Http404()
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    #* annotate => cria o nome do campo temporariamente
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(mostrar=True).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) | Q(categoria__nome__icontains=termo)
    )
    # ? filter( nome_completo like =%% OR telefone like=%%)

    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
