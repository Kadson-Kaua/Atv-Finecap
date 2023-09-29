from django.contrib import admin
from .models import Reserva

# Register your models here.
@admin.register(Reserva)
class StandAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa','quitado',)
