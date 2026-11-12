"""Objetos do domínio: sem dependência de Django ou banco de dados."""
from dataclasses import dataclass
from datetime import date

PRIORIDADES = ("ALTA", "MEDIA", "BAIXA")  # níveis provisórios; confirmar com cliente
ESTADO_INICIAL = "SOLICITADO"  # fluxo completo ainda depende de validação


@dataclass(frozen=True)
class Atendimento:
    nome_cliente: str
    descricao: str
    prioridade: str = "MEDIA"
    prazo_previsto: date | None = None
    estado: str = ESTADO_INICIAL
    id: int | None = None


class DadosInvalidos(ValueError):
    """Dados insuficientes ou incoerentes para registrar um atendimento."""
