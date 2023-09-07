from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Stand
from .forms import ReservaForm
# Create your views here.

def criar_reserva(request):
    if request.method == "POST":

        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_reserva')
    else: 
        form = ReservaForm()

    return render(request, 'reserva.html', {'form': form})

def listar_reserva(request):
    reservas = Reserva.objects.all() 
    context = {'reservas': reservas}
    return render(request, 'lista_reservas.html', context)

def remover_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar_reserva')

def reserva_detalhe(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, 'reserva_detalhe.html', context)