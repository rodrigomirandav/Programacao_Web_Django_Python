from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core.models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação web com Django',
        'outro': 'Django é massa!',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }

    return render(request, 'produto.html',context)


def error404(request, exception):
    return render(request,'404.html')