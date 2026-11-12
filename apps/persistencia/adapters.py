"""Adapter: traduz objetos de domínio para o Django ORM e vice-versa."""
from apps.atendimentos.domain import Atendimento
from .models import AtendimentoModel


def _para_dominio(registro: AtendimentoModel) -> Atendimento:
    return Atendimento(
        id=registro.pk,
        nome_cliente=registro.nome_cliente,
        descricao=registro.descricao,
        prioridade=registro.prioridade,
        estado=registro.estado,
        prazo_previsto=registro.prazo_previsto,
    )


class DjangoAtendimentoAdapter:
    def salvar(self, atendimento: Atendimento) -> Atendimento:
        registro = AtendimentoModel.objects.create(
            nome_cliente=atendimento.nome_cliente,
            descricao=atendimento.descricao,
            prioridade=atendimento.prioridade,
            estado=atendimento.estado,
            prazo_previsto=atendimento.prazo_previsto,
        )
        return _para_dominio(registro)

    def listar(self) -> list[Atendimento]:
        return [_para_dominio(r) for r in AtendimentoModel.objects.all()]
