"""Strategy: política de ordenação desacoplada do domínio Django e do ORM."""
from typing import Protocol, TypeVar


class ItemPriorizavel(Protocol):
    @property
    def prioridade(self) -> str: ...

    @property
    def id(self) -> int | None: ...


T = TypeVar("T", bound=ItemPriorizavel)


class PoliticaPrioridade(Protocol):
    def chave_ordenacao(self, atendimento: ItemPriorizavel) -> tuple[int, int]: ...


class PrioridadeManual:
    """Ordena prioridade digitada; não calcula critérios de risco/tempo."""
    ORDEM = {"ALTA": 0, "MEDIA": 1, "BAIXA": 2}

    def chave_ordenacao(self, atendimento: ItemPriorizavel) -> tuple[int, int]:
        # Desempate provisório pela ordem de cadastro (id menor primeiro).
        return (self.ORDEM[atendimento.prioridade], atendimento.id or 0)


class ServicoDePriorizacao:
    def __init__(self, politica: PoliticaPrioridade):
        self.politica = politica

    def ordenar(self, atendimentos: list[T]) -> list[T]:
        return sorted(atendimentos, key=self.politica.chave_ordenacao)
