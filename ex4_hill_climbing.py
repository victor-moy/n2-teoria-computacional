import random
from typing import Dict, List, Optional, Tuple

from dados import CAPACIDADE, TAREFAS, avaliar_solucao, imprimir_resultado
from ex2_greedy import greedy_knapsack


def gerar_vizinhos(individuo: List[int]) -> List[List[int]]:
    """Gera todos os n vizinhos (soluções a 1 bit de distância)."""
    vizinhos = []

    for i in range(len(individuo)):
        # copia o individuo e inverte o bit na posição i
        vizinho = individuo[:]
        vizinho[i] = 1 - vizinho[i]
        vizinhos.append(vizinho)

    return vizinhos


def hill_climbing(
    tarefas: List[Dict],
    capacidade: int,
    solucao_inicial: Optional[List[int]] = None,
    max_iter: int = 1000,
    verbose: bool = False
) -> Tuple[List[int], int, int]:
    """Busca local: melhora iterativamente trocando 1 bit por vez.

    Retorna: (melhor_individuo, melhor_valor, n_iteracoes)
    """
    # começa pelo greedy se não receber solução inicial
    if solucao_inicial is None:
        atual, _ = greedy_knapsack(tarefas, capacidade)
    else:
        atual = solucao_inicial[:]

    atual_valor = avaliar_solucao(atual, tarefas, capacidade)
    n_iter = 0

    for it in range(max_iter):
        vizinhos = gerar_vizinhos(atual)

        # pega o melhor vizinho
        melhor_viz = max(vizinhos, key=lambda v: avaliar_solucao(v, tarefas, capacidade))
        melhor_viz_valor = avaliar_solucao(melhor_viz, tarefas, capacidade)

        if melhor_viz_valor > atual_valor:
            # tem um vizinho melhor, move pra ele
            atual = melhor_viz
            atual_valor = melhor_viz_valor
            n_iter = it + 1

            if verbose:
                print(f"  iteração {it + 1}: valor melhorou para {atual_valor}")
        else:
            # nenhum vizinho é melhor — chegou num mínimo local
            n_iter = it
            break

    return atual, atual_valor, n_iter


def hill_climbing_restarts(
    tarefas: List[Dict],
    capacidade: int,
    n_restarts: int = 5,
    max_iter: int = 1000
) -> Tuple[List[int], int]:
    """DESAFIO: hill climbing com múltiplos pontos de partida aleatórios.

    A ideia é tentar escapar de mínimos locais reiniciando de lugares diferentes.
    """
    n = len(tarefas)

    # primeira rodada começa do greedy
    melhor_individuo, melhor_valor, _ = hill_climbing(tarefas, capacidade, max_iter=max_iter)

    for restart in range(n_restarts - 1):
        # partida aleatória
        inicio_aleatorio = [random.randint(0, 1) for _ in range(n)]
        individuo, valor, _ = hill_climbing(
            tarefas, capacidade,
            solucao_inicial=inicio_aleatorio,
            max_iter=max_iter
        )

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_individuo = individuo

    return melhor_individuo, melhor_valor


if __name__ == "__main__":
    print("=" * 50)
    print("Ex 4 — Hill Climbing (Busca Local)")
    print("=" * 50)

    individuo, valor, iters = hill_climbing(TAREFAS, CAPACIDADE, verbose=True)
    imprimir_resultado(individuo, TAREFAS, f"Hill Climbing (valor = {valor}, iters = {iters})")

    # verifica que não estourou a capacidade
    custo = sum(TAREFAS[i]["custo"] for i in range(len(individuo)) if individuo[i] == 1)
    assert custo <= CAPACIDADE, "ERRO: estourou a capacidade!"
    assert valor > 0, "ERRO: valor zero"
    print("\n✅ Ex 4 OK")

    # demonstração de mínimos locais com 5 partidas diferentes
    print("\n--- Mínimos Locais: 5 partidas aleatórias ---")
    random.seed(7)
    resultados = []

    for i in range(5):
        inicio = [random.randint(0, 1) for _ in range(len(TAREFAS))]
        _, val, _ = hill_climbing(TAREFAS, CAPACIDADE, solucao_inicial=inicio)
        resultados.append(val)
        print(f"  Partida {i + 1}: valor = {val}")

    print(f"\n  Variação: {max(resultados) - min(resultados)}")
    print("  Os valores diferentes mostram que o hill climbing fica preso em mínimos locais!")

    # DESAFIO: com restarts
    print("\n--- DESAFIO: hill climbing com 5 restarts ---")
    random.seed(42)
    melhor_ind, melhor_val = hill_climbing_restarts(TAREFAS, CAPACIDADE, n_restarts=5)
    imprimir_resultado(melhor_ind, TAREFAS, f"Melhor com restarts (valor = {melhor_val})")
