import unittest
from apps.atendimentos.domain import Atendimento
from apps.priorizacao.policies import PrioridadeManual, ServicoDePriorizacao


class TestePriorizacaoPura(unittest.TestCase):
    def test_ordena_por_prioridade_manual(self):
        entradas = [
            Atendimento("Cliente A", "Reparo A", "BAIXA", id=1),
            Atendimento("Cliente B", "Reparo B", "ALTA", id=2),
            Atendimento("Cliente C", "Reparo C", "MEDIA", id=3),
        ]
        resultado = ServicoDePriorizacao(PrioridadeManual()).ordenar(entradas)
        self.assertEqual([a.id for a in resultado], [2, 3, 1])

    def test_desempate_pelo_id_na_mesma_prioridade(self):
        entradas = [Atendimento("B", "Serviço B", "ALTA", id=3), Atendimento("A", "Serviço A", "ALTA", id=2)]
        resultado = ServicoDePriorizacao(PrioridadeManual()).ordenar(entradas)
        self.assertEqual([a.id for a in resultado], [2, 3])
