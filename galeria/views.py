from django.shortcuts import get_object_or_404, render, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você deve estar logado!")
        return redirect('login')
    
    #dados = {
    #1: {"nome": "Nebulosa de Carina",
    #    "legenda": "webtelescope.org / NASA / James Web"},
    #2: {"nome": "Galáxia NGC 1079",
    #    "legenda": "nasa.org / NASA / Hubble"}
#}
    # return render(request, 'galeria/index.html', {"cards": dados})
    
    #fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você deve estar logado!")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})