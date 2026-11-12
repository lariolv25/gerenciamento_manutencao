# Migração inicial do protótipo — manter versionada.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="AtendimentoModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome_cliente", models.CharField(max_length=120)),
                ("descricao", models.TextField()),
                ("prioridade", models.CharField(choices=[("ALTA", "Alta (provisória)"), ("MEDIA", "Média (provisória)"), ("BAIXA", "Baixa (provisória)")], default="MEDIA", max_length=5)),
                ("prazo_previsto", models.DateField(blank=True, null=True)),
                ("estado", models.CharField(default="SOLICITADO", max_length=24)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-criado_em"], "verbose_name": "atendimento", "verbose_name_plural": "atendimentos"},
        ),
    ]
