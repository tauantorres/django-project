from django.urls import path
from. views import HomePage, HomeFilmes, FilmeDetalhe

# Criar o namespace para a aplicação
app_name = 'filme'

# Criar a lista de URLs para esse app
urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', FilmeDetalhe.as_view(), name='filmedetalhe')
]
