from django.urls import path
from. views import HomePage, HomeFilmes, FilmeDetalhe

app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', FilmeDetalhe.as_view(), name='filmedetalhe')
]