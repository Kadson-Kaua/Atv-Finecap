from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission

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
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['is_editing'] = False  # Indica que não estamos editando
        return context


class ReservasListView(LoginRequiredMixin, generic.ListView):
    model = Reserva
    template_name = "lista_reservas.html"
    paginate_by = 2

    def get_queryset(self):
    # Retorna apenas as reservas do usuário logado
        return Reserva.objects.filter(user=self.request.user)

class ReservaDeleteView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin,generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reservas:lista_reservas")
    success_message = "reserva cancelada com sucesso!!"
  
class ReservaUpdateView(GerentePermission, LoginRequiredMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reservas:lista_reservas")
    template_name = "reserva.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_editing'] = True  # Indica que estamos editando
        return context

class ReservaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "reserva_detalhe.html"  