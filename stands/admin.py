from django.contrib import admin
from .models import Stand 

# Register your models here.
@admin.register(Stand)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('localizacao','valor',)