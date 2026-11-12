import unittest
from apps.atendimentos.domain import Atendimento, DadosInvalidos
from apps.atendimentos.services import ServicoAtendimentos
from apps.priorizacao.policies import PrioridadeManual


class RepositorioFalso:
    def __init__(self):
        self.itens = []

    def salvar(self, atendimento):
        gravado = Atendimento(atendimento.nome_cliente, atendimento.descricao, atendimento.prioridade, atendimento.prazo_previsto, atendimento.estado, id=len(self.itens) + 1)
        self.itens.append(gravado)
        return gravado

    def listar(self):
        return list(self.itens)


class TesteServicosSemBanco(unittest.TestCase):
    def setUp(self):
        self.servico = ServicoAtendimentos(RepositorioFalso(), PrioridadeManual())

    def test_registra_atendimento(self):
        resultado = self.servico.registrar(" Cliente exemplo ", " Trocar peça ", "ALTA")
        self.assertEqual(resultado.nome_cliente, "Cliente exemplo")
        self.assertEqual(resultado.estado, "SOLICITADO")

    def test_recusa_prioridade_invalida(self):
        with self.assertRaises(DadosInvalidos):
            self.servico.registrar("Cliente", "Serviço", "URGENTISSIMA")

    def test_recusa_nome_vazio(self):
        with self.assertRaises(DadosInvalidos):
            self.servico.registrar(" ", "Serviço", "MEDIA")
