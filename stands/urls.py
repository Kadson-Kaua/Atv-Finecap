
from django.contrib import admin
from django.urls import path
from stands.views import StandCreateView, StandDeleteView, StandListView, StandUpdateView  

app_name = "stands"

urlpatterns = [
    path('lista_stands/', StandListView.as_view(), name='lista_stands'),
    path('criar_stand/', StandCreateView.as_view(), name="criar_stand"),
    path('remover_stand/<int:pk>/', StandDeleteView.as_view(), name="remover_stand"),
    path('update_stand/<int:pk>/', StandUpdateView.as_view(), name="editar_stand"),

]

