from typing import Dict, List, Tuple

from dados import CAPACIDADE, TAREFAS, imprimir_resultado
from ex1_brute_force import busca_exaustiva


def greedy_knapsack(tarefas: List[Dict], capacidade: int) -> Tuple[List[int], int]:
    """Heurística gulosa: ordena por ROI decrescente e adiciona tarefas.

    ROI = valor / custo  (quanto valor cada SP gera).
    Complexidade: O(n log n).
    """
    n = len(tarefas)
    individuo = [0] * n
    capacidade_restante = capacidade

    # ordena pelo maior bang-for-buck, mas preserva o índice original
    # (preciso do índice original pra marcar o individuo corretamente)
    indices_ordenados = sorted(
        range(n),
        key=lambda i: tarefas[i]["valor"] / tarefas[i]["custo"],
        reverse=True
    )

    for i in indices_ordenados:
        # adiciona a tarefa se ainda couber
        if tarefas[i]["custo"] <= capacidade_restante:
            individuo[i] = 1
            capacidade_restante -= tarefas[i]["custo"]

    valor_total = sum(tarefas[i]["valor"] for i in range(n) if individuo[i] == 1)
    return individuo, valor_total


if __name__ == "__main__":
    print("=" * 50)
    print("Ex 2 — Heurística Gulosa (Greedy)")
    print("=" * 50)

    individuo, valor = greedy_knapsack(TAREFAS, CAPACIDADE)
    imprimir_resultado(individuo, TAREFAS, f"Solução Greedy (valor = {valor})")
    print("\n✅ Ex 2 OK")

    # comparação greedy vs brute force usando só as 6 primeiras tarefas
    print("\n--- Comparação: Greedy vs Brute Force (6 tarefas, cap=20) ---")
    sub = TAREFAS[:6]
    cap = 20

    _, val_bf = busca_exaustiva(sub, cap)
    _, val_gr = greedy_knapsack(sub, cap)

    print(f"  Brute Force = {val_bf}")
    print(f"  Greedy      = {val_gr}")
    print(f"  Gap         = {val_bf - val_gr}")

    if val_bf == val_gr:
        print("  Nesse caso o greedy acertou o ótimo!")
    else:
        print("  Greedy ficou abaixo do ótimo — exemplo de falha da heurística")

    # DESAFIO: instância onde greedy falha
    # Exemplo clássico: 2 itens pesados com ROI alto vs combinação de leves
    print("\n--- DESAFIO: instância onde greedy falha ---")
    instancia_falha = [
        {"nome": "Item A", "custo": 10, "valor": 60},   # ROI = 6.0 (melhor)
        {"nome": "Item B", "custo": 10, "valor": 55},   # ROI = 5.5
        {"nome": "Item C", "custo": 11, "valor": 65},   # ROI = 5.9
    ]
    cap_falha = 20

    ind_gr, val_gr = greedy_knapsack(instancia_falha, cap_falha)
    ind_bf, val_bf = busca_exaustiva(instancia_falha, cap_falha)

    print(f"  Greedy pegou: custo={sum(instancia_falha[i]['custo'] for i in range(3) if ind_gr[i])}, valor={val_gr}")
    print(f"  Ótimo real  : custo={sum(instancia_falha[i]['custo'] for i in range(3) if ind_bf[i])}, valor={val_bf}")
    print(f"  O greedy escolheu A+B (ROI alto) mas A+C seria melhor!")
