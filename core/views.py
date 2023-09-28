from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Stand
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views

# Create your views here.


class ReservaCreateView(generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Reserva cadastrada!!")
        return super().form_valid(form)



class ReservasListView(generic.ListView):
    model = Reserva
    template_name = "lista_reservas.html"
    paginate_by = 2

class ReservaDeleteView(views.SuccessMessageMixin,generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("lista_reservas")
    success_message = "reserva cancelada com sucesso!!"
    
    #def form_valid(self, form):
     #   messages.error(self.request, "Reserva cancelada!")
     #   return super().form_valid(form)

class ReservaUpdateView(generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        messages.success(self.request, "Atualizado com sucesso!!")
        return super().form_valid(form)


class ReservaDetailView(generic.DetailView):
    model = Reserva
    template_name = "reserva_detalhe.html"  