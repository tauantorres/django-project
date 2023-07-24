from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8]
    filme_destaque = lista_filmes[0]
    return {'lista_filmes_recentes': lista_filmes, 'filme_destaque': filme_destaque}
    
def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacao')[:8]
    return {'lista_filmes_em_alta': lista_filmes}
