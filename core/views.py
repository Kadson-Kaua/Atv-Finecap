from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva, Stand
from .forms import ReservaForm, StandForm
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


  # CRUD STANDS #


class StandCreateView(generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Stand cadastrada!!")
        return super().form_valid(form)

class StandListView(generic.ListView):
    model = Stand
    template_name = "lista_stands.html"
    paginate_by = 2

class StandUpdateView(generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Atualizado com sucesso!!")
        return super().form_valid(form)

class StandDeleteView(views.SuccessMessageMixin,generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("lista_stands")
    success_message = "Stand removido com sucesso!!"