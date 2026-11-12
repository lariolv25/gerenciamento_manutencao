from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("atendimentos/novo/", views.novo_atendimento, name="novo_atendimento"),
]
