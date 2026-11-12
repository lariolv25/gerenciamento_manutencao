from django.contrib import admin
from .models import AtendimentoModel


@admin.register(AtendimentoModel)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ("nome_cliente", "prioridade", "estado", "prazo_previsto", "criado_em")
    search_fields = ("nome_cliente", "descricao")
    list_filter = ("prioridade", "estado")
