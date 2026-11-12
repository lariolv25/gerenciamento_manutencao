from django.test import TestCase
from django.urls import reverse
from apps.persistencia.adapters import DjangoAtendimentoAdapter
from apps.atendimentos.domain import Atendimento
from apps.persistencia.models import AtendimentoModel


class TestesDeIntegracao(TestCase):
    def test_salva_e_recupera_atendimento_via_adapter(self):
        repo = DjangoAtendimentoAdapter()
        salvo = repo.salvar(Atendimento("Cliente Teste", "Troca de tomada", "ALTA"))
        self.assertIsNotNone(salvo.id)
        self.assertEqual(repo.listar()[0].descricao, "Troca de tomada")

    def test_pagina_inicial_carrega(self):
        resposta = self.client.get(reverse("inicio"))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Atendimentos")

    def test_cadastro_por_formulario(self):
        resposta = self.client.post(reverse("novo_atendimento"), {
            "nome_cliente": "Cliente Fictício",
            "descricao": "Revisão de aparelho",
            "prioridade": "ALTA",
            "prazo_previsto": "",
        })
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(AtendimentoModel.objects.count(), 1)
        self.assertEqual(AtendimentoModel.objects.first().estado, "SOLICITADO")

    def test_formulario_invalido_nao_salva(self):
        resposta = self.client.post(reverse("novo_atendimento"), {
            "nome_cliente": "", "descricao": "Revisão", "prioridade": "MEDIA"
        })
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(AtendimentoModel.objects.count(), 0)
