"""Porta para funcionalidades futuras (ADR-006) não validadas com o cliente."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoPlanejamento:
    disponivel: bool
    motivo: str


class ServicoPlanejamento:
    def avaliar_capacidade(self) -> ResultadoPlanejamento:
        return ResultadoPlanejamento(
            disponivel=False,
            motivo="Análise de capacidade ainda não implementada: regras e horas/dia pendentes de validação.",
        )

    def sugerir_prazo(self):
        """Sem estimativa automática até validação da regra de cálculo pelo cliente."""
        return None
