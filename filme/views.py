from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView


class HomePage(TemplateView):
    template_name = 'homepage.html'

class HomeFilmes(ListView):
    model = Filme
    template_name = 'homefilmes.html'
    context_object_name = 'lista_filmes'


# Create your views here.
#def homepage(request: object) -> object:
#    return render(request, 'homepage.html')
# def homefilmes(request: object) -> object:
#     context = dict()
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', context)
