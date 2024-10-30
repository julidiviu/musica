from django.contrib import admin

# Register your models here.
from .models import Banda, Album, Cancion

admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Cancion)