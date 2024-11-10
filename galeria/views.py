from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia

def index(request):
    
    #dados = {
    #1: {"nome": "Nebulosa de Carina",
    #    "legenda": "webtelescope.org / NASA / James Web"},
    #2: {"nome": "Galáxia NGC 1079",
    #    "legenda": "nasa.org / NASA / Hubble"}
#}
    # return render(request, 'galeria/index.html', {"cards": dados})
    
    fotografias = Fotografia.objects.all()
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})