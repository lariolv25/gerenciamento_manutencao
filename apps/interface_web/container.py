"""Ponto único que conecta os casos de uso ao adaptador de persistência."""
from apps.atendimentos.services import ServicoAtendimentos
from apps.persistencia.adapters import DjangoAtendimentoAdapter
from apps.priorizacao.policies import PrioridadeManual


def criar_servico_atendimentos() -> ServicoAtendimentos:
    return ServicoAtendimentos(DjangoAtendimentoAdapter(), PrioridadeManual())
