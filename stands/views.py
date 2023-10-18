from django.shortcuts import render, get_object_or_404, redirect
from .models import Stand
from .forms import StandForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from users.permissions import GerentePermission

class StandCreateView(GerentePermission, LoginRequiredMixin, generic.CreateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Stand cadastrada!!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class StandListView(LoginRequiredMixin, generic.ListView):
    model = Stand
    template_name = "lista_stands.html"
    paginate_by = 2

class StandUpdateView(GerentePermission, LoginRequiredMixin, generic.UpdateView):
    model = Stand
    form_class = StandForm
    success_url = reverse_lazy("stands:lista_stands")
    template_name = "reserva_stand.html"

    def form_valid(self, form):
        messages.success(self.request, "Atualizado com sucesso!!")
        return super().form_valid(form)

class StandDeleteView(GerentePermission, LoginRequiredMixin, views.SuccessMessageMixin,generic.DeleteView):
    model = Stand
    success_url = reverse_lazy("stands:lista_stands")
    success_message = "Stand removido com sucesso!!"