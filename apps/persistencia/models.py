"""Modelo de armazenamento do protótipo, com dados fictícios."""
from django.db import models


class AtendimentoModel(models.Model):
    class Prioridade(models.TextChoices):
        ALTA = "ALTA", "Alta (provisória)"
        MEDIA = "MEDIA", "Média (provisória)"
        BAIXA = "BAIXA", "Baixa (provisória)"

    # O fluxo de estados sugerido pelo professor ainda precisa de validação;
    # inicialmente só se registra a solicitação.
    nome_cliente = models.CharField(max_length=120)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=5, choices=Prioridade.choices, default=Prioridade.MEDIA)
    prazo_previsto = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=24, default="SOLICITADO")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "atendimento"
        verbose_name_plural = "atendimentos"

    def __str__(self):
        return f"{self.nome_cliente} — {self.prioridade}"
