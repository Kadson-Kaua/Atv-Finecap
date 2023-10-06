from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import views
from django.contrib.auth.mixins import LoginRequiredMixin
from reservas.models import Reserva
from stands.models import Stand

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_reservas'] = Reserva.objects.count()
        context['num_stands'] = Stand.objects.count()
        return context

