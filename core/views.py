from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Stand
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

#def criar_reserva(request):
#    if request.method == "POST":
#
#        form = ReservaForm(request.POST, request.FILES)
#        if form.is_valid():
#           form.save()
#           return redirect('listar_reserva')
#    else: 
#        form = ReservaForm()

#    return render(request, 'reserva.html', {'form': form})

class ReservaCreateView(generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("lista_reservas")
  template_name = "reserva.html"

#def listar_reserva(request):
#    reservas = Reserva.objects.all() 
#    context = {'reservas': reservas}
#    return render(request, 'lista_reservas.html', context)

class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "lista_reservas.html"


class ReservaDeleteView(generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("lista_reservas")

class ReservaUpdateView(generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("lista_reservas")
  template_name = "reserva.html"


class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "reserva_detalhe.html"