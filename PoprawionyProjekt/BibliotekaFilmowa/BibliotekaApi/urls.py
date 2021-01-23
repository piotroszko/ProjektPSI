from django.urls import path
from . import views

urlpatterns = [
    path('film-list', views.ListaFilmow.as_view(), name=views.ListaFilmow.name),
    path('recenzje', views.Recenzje.as_view(), name=views.Recenzje.name),
    path('rezyserowie', views.Rezyserowie.as_view(), name=views.Rezyserowie.name),
    path('scenarzysci', views.Scenarzysci.as_view(), name=views.Scenarzysci.name),
    ]
