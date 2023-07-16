from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:3]
    return {'lista_filmes_recentes': lista_filmes}
    
def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacao')[:3]
    return {'lista_filmes_em_alta': lista_filmes}
