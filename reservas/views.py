from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin

class ReservaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:lista_reservas")
    template_name = "reserva.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Define o usuário atual como o proprietário da reserva
        messages.success(self.request, "Reserva cadastrada!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ReservasListView(LoginRequiredMixin, generic.ListView):
    model = Reserva
    template_name = "lista_reservas.html"
    paginate_by = 2

    def get_queryset(self):
    # Retorna apenas as reservas do usuário logado
        return Reserva.objects.filter(user=self.request.user)

class ReservaDeleteView(LoginRequiredMixin, views.SuccessMessageMixin,generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:lista_reservas")
    success_message = "reserva cancelada com sucesso!!"
  
class ReservaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:lista_reservas")
    template_name = "reserva.html"

class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "reserva_detalhe.html"  