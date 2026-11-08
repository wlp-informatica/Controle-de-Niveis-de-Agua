# Controle de Níveis de Água

Atividade de Desenvolvimento de Sistemas I — Agenda 11 (Bibliotecas).

## Objetivo

Simular o monitoramento de um reservatório de água, exibindo uma mensagem colorida para cada um dos cinco níveis.

## Requisitos

- Python 3 instalado.
- Biblioteca `colorama`.

## Instalação

No terminal, dentro da pasta do projeto, execute:

```bash
python -m pip install -r requirements.txt
```

Ou instale diretamente:

```bash
python -m pip install colorama
```

## Execução

```bash
python main.py
```

## Funcionamento

O programa armazena os cinco níveis em uma lista. A função `exibir_alerta()` percorre essa lista, identifica o nível recebido e apresenta a situação com a cor correspondente. `Style.RESET_ALL` restaura o estilo padrão do terminal após cada mensagem.

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

Os níveis simulados estão definidos no código em `niveis_simulados = [1, 2, 3, 4, 5]`.
