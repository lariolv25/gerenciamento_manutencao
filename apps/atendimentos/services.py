"""Casos de uso independentes de views e Django ORM."""
from datetime import date
from .domain import Atendimento, DadosInvalidos, PRIORIDADES
from .ports import RepositorioAtendimento
from apps.priorizacao.policies import PoliticaPrioridade, ServicoDePriorizacao


class ServicoAtendimentos:
    def __init__(self, repositorio: RepositorioAtendimento, politica: PoliticaPrioridade):
        self.repositorio = repositorio
        self.priorizacao = ServicoDePriorizacao(politica)

    def registrar(self, nome_cliente: str, descricao: str, prioridade: str = "MEDIA", prazo_previsto: date | None = None) -> Atendimento:
        nome_cliente, descricao = nome_cliente.strip(), descricao.strip()
        if not nome_cliente or not descricao:
            raise DadosInvalidos("Informe o nome fictício do cliente e a descrição do serviço.")
        if prioridade not in PRIORIDADES:
            raise DadosInvalidos("Prioridade inválida.")
        return self.repositorio.salvar(Atendimento(
            nome_cliente=nome_cliente,
            descricao=descricao,
            prioridade=prioridade,
            prazo_previsto=prazo_previsto,
        ))

    def listar_por_prioridade(self) -> list[Atendimento]:
        return self.priorizacao.ordenar(self.repositorio.listar())
