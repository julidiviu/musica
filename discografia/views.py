from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from discografia.models import Banda, Album, Cancion

# Create your views here.
#BANDA

class BandaListView(ListView):
    model = Banda
    
class BandaDetailView(DetailView):
    model = Banda
    
class BandaCreate(CreateView):
    model = Banda
    fields = '__all__'
    
class BandaUpdate(UpdateView):
    model = Banda
    fields = '__all__'
    
class BandaDelete(DeleteView):
    model = Banda
    success_url = reverse_lazy('banda-list')
       
#ALBUM

class AlbumListView(ListView):
    model = Album
    
class AlbumDetailView(DetailView):
    model = Album
    
class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    
class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'
    
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('album-list')
    
    
#CANCION

class CancionListView(ListView):
    model = Cancion
    
class CancionDetailView(DetailView):
    model = Cancion
    
class CancionCreate(CreateView):
    model = Cancion
    fields = '__all__'
    
class CancionUpdate(UpdateView):
    model = Cancion
    fields = '__all__'
    
class CancionDelete(DeleteView):
    model = Cancion
    success_url = reverse_lazy('cancion-list')