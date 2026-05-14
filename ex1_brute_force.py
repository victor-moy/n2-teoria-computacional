import itertools
from typing import Dict, List, Tuple

from dados import CAPACIDADE, TAREFAS, imprimir_resultado


def busca_exaustiva(tarefas: List[Dict], capacidade: int) -> Tuple[List[int], int]:
    """Encontra a Sprint ótima testando todas as combinações.

    Complexidade: O(2^n) — exponencial.
    """
    n = len(tarefas)
    melhor_individuo = [0] * n
    melhor_valor = 0

    # gera todas as combinações possíveis de 0s e 1s (cada tarefa entra ou não)
    for combo in itertools.product([0, 1], repeat=n):
        custo_atual = 0
        valor_atual = 0

        for i in range(n):
            if combo[i] == 1:
                custo_atual += tarefas[i]["custo"]
                valor_atual += tarefas[i]["valor"]

        # só considera se não estourou a capacidade
        if custo_atual <= capacidade and valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_individuo = list(combo)

    return melhor_individuo, melhor_valor


if __name__ == "__main__":
    print("=" * 50)
    print("Ex 1 — Busca Exaustiva (Brute Force)")
    print("=" * 50)

    individuo, valor = busca_exaustiva(TAREFAS, CAPACIDADE)
    imprimir_resultado(individuo, TAREFAS, f"Melhor combinação encontrada (valor = {valor})")

    # verificação básica
    custo = sum(TAREFAS[i]["custo"] for i in range(len(individuo)) if individuo[i] == 1)
    assert custo <= CAPACIDADE, "ERRO: estourou a capacidade!"
    assert valor > 0, "ERRO: valor zero, algo deu errado"
    print("\n✅ Ex 1 OK")

    # DESAFIO: o que acontece com o tempo quando aumentamos n?
    print("\n--- DESAFIO: testando com 20 tarefas aleatórias ---")
    import random, time
    random.seed(0)
    tarefas_grandes = [
        {"nome": f"task_{i}", "custo": random.randint(1, 10), "valor": random.randint(5, 50)}
        for i in range(20)
    ]
    print("Rodando brute force com n=20... (pode demorar!)")
    t0 = time.perf_counter()
    busca_exaustiva(tarefas_grandes, 30)
    print(f"Tempo com n=20: {(time.perf_counter() - t0):.2f}s")
    print("Repara como fica lento comparado com n=10 — isso é O(2^n) na prática")
