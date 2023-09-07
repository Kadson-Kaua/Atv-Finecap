from django.contrib import admin
from .models import Reserva, Stand 

# Register your models here.
@admin.register(Reserva)
class StandAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa','quitado',)
@admin.register(Stand)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('localizacao','valor',)