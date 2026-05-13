# Dados compartilhados entre os exercícios
# Disciplina: Teoria da Computação

CAPACIDADE = 40  # Story Points máximos na Sprint

TAREFAS = [
    {"nome": "Auth OAuth2",          "custo": 8,  "valor": 40},
    {"nome": "Dashboard métricas",   "custo": 13, "valor": 55},
    {"nome": "Exportar CSV",         "custo": 5,  "valor": 20},
    {"nome": "Refactor serviço X",   "custo": 20, "valor": 35},
    {"nome": "API notificações",     "custo": 10, "valor": 60},
    {"nome": "Upgrade deps",         "custo": 3,  "valor": 15},
    {"nome": "Testes E2E checkout",  "custo": 8,  "valor": 50},
    {"nome": "Rate limiting",        "custo": 6,  "valor": 45},
    {"nome": "Docs OpenAPI",         "custo": 4,  "valor": 25},
    {"nome": "Cache Redis",          "custo": 12, "valor": 70},
]


def avaliar_solucao(individuo, tarefas, capacidade):
    # calcula custo e valor total de uma solução
    # individuo é uma lista de 0s e 1s indicando quais tarefas entram
    custo_total = 0
    valor_total = 0

    for i in range(len(individuo)):
        if individuo[i] == 1:
            custo_total += tarefas[i]["custo"]
            valor_total += tarefas[i]["valor"]

    # se estourou a capacidade, solução inválida
    if custo_total > capacidade:
        return 0

    return valor_total


def imprimir_resultado(individuo, tarefas, label="Resultado"):
    custo_total = 0
    valor_total = 0
    selecionadas = []

    for i in range(len(individuo)):
        if individuo[i] == 1:
            custo_total += tarefas[i]["custo"]
            valor_total += tarefas[i]["valor"]
            selecionadas.append(tarefas[i]["nome"])

    print(f"\n{label}")
    print(f"  Tarefas selecionadas : {selecionadas}")
    print(f"  Custo total          : {custo_total} SP")
    print(f"  Valor total (ROI)    : {valor_total}")
