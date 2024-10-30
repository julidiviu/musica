"""
URL configuration for musica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from discografia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #banda
    path('banda/',views.BandaListView.as_view(),name='banda-list'),
    path('banda/<int:pk>/detail/',views.BandaDetailView.as_view(),name='banda-detail'),
    path('banda/create/',views.BandaCreate.as_view(), name='banda-create'),
    path('banda/<int:pk>/update',views.BandaUpdate.as_view(), name='banda-update'),
    path('banda/<int:pk>/delete',views.BandaDelete.as_view(), name='banda-delete'),
    #album
    path('album/',views.AlbumListView.as_view(),name='album-list'),
    path('album/<int:pk>/detail/',views.AlbumDetailView.as_view(),name='album-detail'),
    path('album/create/',views.AlbumCreate.as_view(), name='album-create'),
    path('album/<int:pk>/update',views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete',views.AlbumDelete.as_view(), name='album-delete'),
    #cancion
    path('cancion/',views.CancionListView.as_view(),name='cancion-list'),
    path('cancion/<int:pk>/detail/',views.CancionDetailView.as_view(),name='cancion-detail'),
    path('cancion/create/',views.CancionCreate.as_view(), name='cancion-create'),
    path('cancion/<int:pk>/update',views.CancionUpdate.as_view(), name='cancion-update'),
    path('cancion/<int:pk>/delete',views.CancionDelete.as_view(), name='cancion-delete'),
]

