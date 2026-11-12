from django.contrib import messages
from django.shortcuts import redirect, render
from .container import criar_servico_atendimentos
from .forms import NovoAtendimentoForm


def inicio(request):
    atendimentos = criar_servico_atendimentos().listar_por_prioridade()
    return render(request, "interface_web/inicio.html", {"atendimentos": atendimentos})


def novo_atendimento(request):
    if request.method == "POST":
        form = NovoAtendimentoForm(request.POST)
        if form.is_valid():
            criar_servico_atendimentos().registrar(**form.cleaned_data)
            messages.success(request, "Atendimento fictício registrado com sucesso.")
            return redirect("inicio")
    else:
        form = NovoAtendimentoForm()
    return render(request, "interface_web/novo_atendimento.html", {"form": form})
