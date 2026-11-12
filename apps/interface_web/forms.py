from django import forms


class NovoAtendimentoForm(forms.Form):
    nome_cliente = forms.CharField(max_length=120, label="Nome fictício do cliente")
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}), label="Serviço solicitado")
    prioridade = forms.ChoiceField(
        choices=[("ALTA", "Alta (provisória)"), ("MEDIA", "Média (provisória)"), ("BAIXA", "Baixa (provisória)")],
        label="Prioridade (definição manual provisória)",
        initial="MEDIA",
    )
    prazo_previsto = forms.DateField(
        required=False,
        label="Prazo previsto (opcional)",
        widget=forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        input_formats=["%Y-%m-%d"],
    )
