from django.urls import path
#from. views import homepage, homefilmes
from. views import HomePage, HomeFilmes

urlpatterns = [
    #path('', homepage),
    path('', HomePage.as_view()),
    path('filmes/', HomeFilmes.as_view()),
]