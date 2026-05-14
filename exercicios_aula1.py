import time

from dados import CAPACIDADE, TAREFAS, imprimir_resultado
from ex1_brute_force import busca_exaustiva
from ex2_greedy import greedy_knapsack


if __name__ == "__main__":
    print("=" * 55)
    print("  Teoria da Computação — Exercícios Aula 1")
    print("=" * 55)

    # --- Ex 1 ---
    print("\n\n[EX 1] Busca Exaustiva (Brute Force)")
    print("-" * 40)
    t0 = time.perf_counter()
    ind, val = busca_exaustiva(TAREFAS, CAPACIDADE)
    tempo_bf = (time.perf_counter() - t0) * 1000

    custo = sum(TAREFAS[i]["custo"] for i in range(len(ind)) if ind[i] == 1)
    assert custo <= CAPACIDADE
    assert val > 0
    imprimir_resultado(ind, TAREFAS, f"Solução ótima — valor = {val}  ({tempo_bf:.2f}ms)")
    print("✅ Ex 1 OK")

    # --- Ex 2 ---
    print("\n\n[EX 2] Heurística Gulosa (Greedy)")
    print("-" * 40)
    t0 = time.perf_counter()
    ind_gr, val_gr = greedy_knapsack(TAREFAS, CAPACIDADE)
    tempo_gr = (time.perf_counter() - t0) * 1000

    imprimir_resultado(ind_gr, TAREFAS, f"Solução greedy — valor = {val_gr}  ({tempo_gr:.4f}ms)")

    # comparação direta
    sub, cap6 = TAREFAS[:6], 20
    _, val_bf6 = busca_exaustiva(sub, cap6)
    _, val_gr6 = greedy_knapsack(sub, cap6)
    print(f"\n  Comparação (6 tarefas, cap=20):")
    print(f"    Brute Force = {val_bf6}  |  Greedy = {val_gr6}  |  gap = {val_bf6 - val_gr6}")
    print("✅ Ex 2 OK")
