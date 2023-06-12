from django.urls import path

from .views import OperaListView, OperaDetailView, ArtistaListView, ArtistaDetailView, CollezioneListView, CollezioneDetailView, homePageView
from django.views.generic import DetailView
from .models import Artista, Opera, Collezione
from . import views



urlpatterns=[
path("", homePageView, name="home"),

path("opera/", OperaListView.as_view(), name="opera"),
path("opera/<int:pk>/", OperaDetailView.as_view(), name="opera_detail"),

path("artista/", ArtistaListView.as_view(), name="artista" ),
path("artista/<int:pk>/", ArtistaDetailView.as_view(), name="artista_detail"),

path("collezione/", CollezioneListView.as_view(), name="collezione" ),
path("collezione/<int:pk>/", CollezioneDetailView.as_view(), name="collezione_detail"),

path("contattaci/", views.add_modifiche, name='contattaci'),
path("add_artista/", views.add_artista, name='add_artista'),
path("add_opera/", views.add_opera, name='add_opera'),
path("add_collezione/", views.add_collezione, name='add_collezione'),

path('update_artista/<artista_id>/', views.update_artista, name='update_artista'),
path('update_collezione/<collezione_id>/', views.update_collezione, name='update_collezione'),
path('update_opera/<opera_id>/', views.update_opera, name='update_opera'),

path('delete_artista/<artista_id>/', views.delete_artista, name='delete_artista'),
path('deletesure_artista/<artista_id>/', views.deletesure_artista, name='deletesure_artista'),
path('delete_collezione/<collezione_id>/', views.delete_collezione, name='delete_collezione'),
path('deletesure_collezione/<collezione_id>/', views.deletesure_collezione, name='deletesure_collezione'),
path('delete_opera/<opera_id>/', views.delete_opera, name='delete_opera'),

path('search_artista/', views.search_artista, name="search_artista"),
path('search_collezione/', views.search_collezione, name="search_collezione"),
path('search_opera/', views.search_opera, name="search_opera"),
]