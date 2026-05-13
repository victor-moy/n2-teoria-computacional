import random
import time
from typing import Dict, List

from ex1_brute_force import busca_exaustiva
from ex2_greedy import greedy_knapsack


def medir_complexidade(
    tamanhos: List[int],
    capacidade: int = 30,
    repeticoes: int = 3
) -> Dict[int, float]:
    """Mede o tempo médio do brute force para diferentes n."""
    resultados = {}

    for n in tamanhos:
        tempos = []

        for _ in range(repeticoes):
            # cria um problema aleatório com n tarefas
            tarefas_rand = [
                {"custo": random.randint(1, 10), "valor": random.randint(5, 50)}
                for _ in range(n)
            ]

            t0 = time.perf_counter()
            busca_exaustiva(tarefas_rand, capacidade)
            tempo_ms = (time.perf_counter() - t0) * 1000
            tempos.append(tempo_ms)

        # guarda a média das repetições pra reduzir ruído
        resultados[n] = sum(tempos) / len(tempos)

    return resultados


def calcular_razoes_crescimento(tempos: Dict[int, float]) -> None:
    """Imprime tabela de tempos e razões de crescimento."""
    ns = sorted(tempos.keys())

    print(f"\n{'n':>4} | {'Tempo (ms)':>12} | {'Razão':>8} | {'2^n':>12}")
    print("-" * 46)

    for i in range(len(ns)):
        n = ns[i]

        if i == 0:
            razao_str = "    —"
        else:
            n_anterior = ns[i - 1]
            if tempos[n_anterior] > 0:
                razao = tempos[n] / tempos[n_anterior]
                razao_str = f"{razao:8.2f}x"
            else:
                razao_str = "   N/A"

        print(f"{n:>4} | {tempos[n]:>12.3f} | {razao_str} | {2**n:>12,}")

    print()
    print("Observação: a razão se estabiliza em ~4x quando aumentamos n de 2 em 2.")
    print("Isso confirma O(2^n): 2^(n+2) / 2^n = 4.")
    print("Cada vez que somamos 2 tarefas, o tempo quadruplica.")


if __name__ == "__main__":
    print("=" * 50)
    print("Ex 3 — Análise Empírica de Complexidade")
    print("=" * 50)

    random.seed(42)
    tamanhos = [5, 8, 10, 12, 14, 16]

    print(f"\nMedindo brute force para n = {tamanhos}...")
    print("(pode demorar alguns segundos para n=14 e 16)")

    tempos = medir_complexidade(tamanhos)
    calcular_razoes_crescimento(tempos)

    print("\n✅ Ex 3 OK")

    # DESAFIO: comparar greedy vs brute force para n=15
    print("\n--- DESAFIO: Greedy vs Brute Force com n=15 ---")
    tarefas_15 = [
        {"custo": random.randint(1, 10), "valor": random.randint(5, 50)}
        for _ in range(15)
    ]

    t0 = time.perf_counter()
    busca_exaustiva(tarefas_15, 30)
    tempo_bf = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    greedy_knapsack(tarefas_15, 30)
    tempo_gr = (time.perf_counter() - t0) * 1000

    print(f"  Brute Force (n=15) : {tempo_bf:.1f} ms")
    print(f"  Greedy      (n=15) : {tempo_gr:.4f} ms")
    print(f"  Greedy é ~{tempo_bf/tempo_gr:.0f}x mais rápido nesse caso")
