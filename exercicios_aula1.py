import random
import time

from dados import CAPACIDADE, TAREFAS, imprimir_resultado
from ex1_brute_force import busca_exaustiva
from ex2_greedy import greedy_knapsack
from ex3_complexidade import calcular_razoes_crescimento, medir_complexidade
from ex4_hill_climbing import hill_climbing, hill_climbing_restarts


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

    # --- Ex 3 ---
    print("\n\n[EX 3] Análise Empírica de Complexidade")
    print("-" * 40)
    random.seed(42)
    tamanhos = [5, 8, 10, 12, 14, 16]
    print(f"Medindo brute force para n = {tamanhos}...")
    print("(pode demorar alguns segundos para n=14 e 16)")
    tempos = medir_complexidade(tamanhos)
    calcular_razoes_crescimento(tempos)

    print("\n--- DESAFIO: Greedy vs Brute Force com n=15 ---")
    tarefas_15 = [
        {"custo": random.randint(1, 10), "valor": random.randint(5, 50)}
        for _ in range(15)
    ]
    t0 = time.perf_counter()
    busca_exaustiva(tarefas_15, 30)
    tempo_bf15 = (time.perf_counter() - t0) * 1000
    t0 = time.perf_counter()
    greedy_knapsack(tarefas_15, 30)
    tempo_gr15 = (time.perf_counter() - t0) * 1000
    print(f"  Brute Force (n=15) : {tempo_bf15:.1f} ms")
    print(f"  Greedy      (n=15) : {tempo_gr15:.4f} ms")
    print(f"  Greedy é ~{tempo_bf15/tempo_gr15:.0f}x mais rápido nesse caso")
    print("✅ Ex 3 OK")

    # --- Ex 4 ---
    print("\n\n[EX 4] Hill Climbing (Busca Local)")
    print("-" * 40)
    individuo, valor, iters = hill_climbing(TAREFAS, CAPACIDADE, verbose=True)
    imprimir_resultado(individuo, TAREFAS, f"Hill Climbing (valor = {valor}, iters = {iters})")

    custo_hc = sum(TAREFAS[i]["custo"] for i in range(len(individuo)) if individuo[i] == 1)
    assert custo_hc <= CAPACIDADE, "ERRO: estourou a capacidade!"
    assert valor > 0, "ERRO: valor zero"

    print("\n--- Mínimos Locais: 5 partidas aleatórias ---")
    random.seed(7)
    resultados_hc = []
    for i in range(5):
        inicio = [random.randint(0, 1) for _ in range(len(TAREFAS))]
        _, val_hc, _ = hill_climbing(TAREFAS, CAPACIDADE, solucao_inicial=inicio)
        resultados_hc.append(val_hc)
        print(f"  Partida {i + 1}: valor = {val_hc}")
    print(f"\n  Variação: {max(resultados_hc) - min(resultados_hc)}")
    print("  Os valores diferentes mostram que o hill climbing fica preso em mínimos locais!")

    print("\n--- DESAFIO: hill climbing com 5 restarts ---")
    random.seed(42)
    melhor_ind, melhor_val = hill_climbing_restarts(TAREFAS, CAPACIDADE, n_restarts=5)
    imprimir_resultado(melhor_ind, TAREFAS, f"Melhor com restarts (valor = {melhor_val})")
    print("✅ Ex 4 OK")
