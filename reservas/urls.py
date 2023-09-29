from django.contrib import admin
from django.urls import path
from reservas.views import ReservaCreateView, ReservaDeleteView, ReservaDetailView, ReservasListView, ReservaUpdateView

app_name = "resevas"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reserva/", ReservaCreateView.as_view(), name="reserva"),
    path('', ReservasListView.as_view(), name='lista_reservas'),
    path('remover_reserva/<int:pk>/', ReservaDeleteView.as_view(), name="remover_reserva"),
    path('reserva_detalhe/<int:pk>/', ReservaDetailView.as_view(), name='reserva_detalhe'),
    path('update/<int:pk>/', ReservaUpdateView.as_view(), name="editar"),
    ]