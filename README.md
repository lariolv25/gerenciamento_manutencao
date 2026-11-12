# Sistema de Gerenciamento de Serviços de Manutenção

**CSI410 — Engenharia de Software II · Etapa 2 · Esqueleto acadêmico**

Este projeto é um **protótipo local** em Python/Django 6.1.3 com SQLite. Implementa uma
página inicial, um formulário de cadastro de atendimentos fictícios, persistência com Django
ORM e ordenação por prioridade **manual provisória** (Alta, Média, Baixa). O cálculo automático
de risco/tempo, a capacidade diária, os conflitos e as transições entre estados **não estão
implementados**: precisam de validação com o cliente e serão incrementos posteriores.

## 1. Requisitos

- Windows 10/11 com **Python 3.12, 3.13, 3.14 ou 3.15** instalado (recomenda-se 3.14).
- VS Code, com extensão Python da Microsoft.
- Conexão à internet para instalar as dependências pela primeira vez.

## 2. Executar no Windows — VS Code / PowerShell

1. Extraia o ZIP e abra a pasta `gerenciamento_manutencao` no VS Code (**Arquivo > Abrir Pasta**).
2. Abra o terminal integrado (**Terminal > Novo Terminal**).
3. Execute na pasta do arquivo `manage.py`:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test tests -v 2
.\.venv\Scripts\python.exe manage.py runserver
```

4. Abra **http://127.0.0.1:8000/** no navegador.
5. Clique em **Novo atendimento**, use exclusivamente nomes fictícios e salve.
6. Confira a listagem ordenada por prioridade informada.
7. Para interromper o servidor, pressione `Ctrl + C` no terminal.

**Não é necessário ativar `.venv`**: os comandos chamam diretamente o Python do ambiente
virtual e não dependem da política de execução do PowerShell.

Se `py` não for reconhecido, instale o Python pelo site oficial e habilite o iniciador;
como alternativa use `python -m venv .venv` caso `python --version` funcione.
Se uma versão anterior do Python estiver selecionada, veja no VS Code:
`Ctrl+Shift+P` > `Python: Select Interpreter` > `.venv`.

## 3. Banco de dados

SQLite cria `db.sqlite3` localmente após `migrate`. O arquivo **não deve entrar no Git**.
A migração `apps/persistencia/migrations/0001_initial.py` é versionada.
Se alterar os modelos mais tarde, execute:

```powershell
.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate
```

## 4. Admin do Django (opcional)

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Acesse **http://127.0.0.1:8000/admin/**.

## 5. Arquitetura (proposta de Etapa 2)

```text
config/                 Django settings e URLs
apps/interface_web/     Views, formulários, templates e ponto de composição
apps/atendimentos/      Modelo de domínio, casos de uso e porta de repositório
apps/priorizacao/       Strategy e prioridade manual (sem Django ORM)
apps/planejamento/      Contratos não implementados de capacidade e sugestão de prazo
apps/persistencia/      Django ORM, migração e Adapter de repositório
templates/              HTML responsivo e acessível
static/                 CSS
tests/                  Testes de domínio, serviço e integração
docs/adr/               Relação com as decisões arquiteturais propostas
```

**Dependências principais:** `interface_web` cria o `ServicoAtendimentos` e injeta
`DjangoAtendimentoAdapter` + `PrioridadeManual`; os casos de uso dependem de um contrato
de repositório, e a regra de prioridade não importa Django. Sem regra automática de recusa.

**ADRs:** o documento externo contém as justificativas completas. Consulte `docs/adr/README.md`.

## 6. Testes e evidências

O comando `manage.py test tests -v 2` usa uma base de testes temporária do Django.
No terminal, copie a saída real dos testes; não invente status. Para a entrega, registre:

- Print de `manage.py check` e resultado de `manage.py test tests -v 2`.
- Print da página inicial e formulário.
- URL do repositório e histórico de commits efetivamente realizados.
- Breve explicação de como pastas, testes e código se relacionam aos ADRs.

**Alternativa sem Django instalado para conferir apenas a lógica pura:**

```powershell
py -m unittest tests.test_priorizacao tests.test_servicos tests.test_planejamento -v
```

Essa alternativa não substitui executar o servidor nem os testes de integração.

## 7. Git / GitHub

Na pasta do projeto, depois de conferir os arquivos:

```powershell
git init
git add .
git commit -m "Etapa 2: esqueleto Django e arquitetura modular"
```

Crie um repositório vazio na sua conta GitHub, depois substitua a URL abaixo pela URL real:

```powershell
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

Nunca publique `.venv`, `db.sqlite3`, senhas ou dados reais do cliente.

## 8. Limitações importantes

- Desenvolvimento local somente. `DEBUG=True` e chave padrão não são seguros para produção.
- Sem autenticação para uso público, autorização por perfis, segurança de produção ou hospedagem.
- Os níveis de prioridade são **provisórios**, sem pesos/algoritmo automático validados.
- O campo `estado` é criado como `SOLICITADO`, sem transições implementadas.
- Sem cálculo de capacidade diária, bloqueio de agendamento, aviso de conflito ou sugestão real de prazo.
- Interface básica voltada à demonstração do esqueleto, ainda não testada com o cliente.

## 9. Declaração de IA

O projeto foi elaborado com auxílio do ChatGPT para ajudar a implementar o esqueleto, estrutura,
formulários, testes e instruções do código. Sou responsável por executar e validar localmente,
registrar evidências e conferir que a implementação está alinhada às decisões aprovadas.
