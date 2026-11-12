import unittest
from apps.planejamento.services import ServicoPlanejamento


class TestePlanejamentoNaoImplementado(unittest.TestCase):
    def test_nao_inventa_capacidade_ou_prazo(self):
        planejamento = ServicoPlanejamento()
        self.assertFalse(planejamento.avaliar_capacidade().disponivel)
        self.assertIsNone(planejamento.sugerir_prazo())
