"""Contrato de persistência independente do Django ORM (ADR-005, Adapter)."""
from typing import Protocol
from .domain import Atendimento


class RepositorioAtendimento(Protocol):
    def salvar(self, atendimento: Atendimento) -> Atendimento:
        ...

    def listar(self) -> list[Atendimento]:
        ...
