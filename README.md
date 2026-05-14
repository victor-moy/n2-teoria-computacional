# Teoria da Computação — Sprint Planning como Knapsack

## Alunos

Jhessica Alves - Laíza Silva - Victor Moy

---

Exercícios práticos de otimização computacional para a disciplina de Teoria da Computação (Engenharia de Software).

## Sobre o problema

O problema modelado é o **Sprint Planning como Knapsack**: dado um conjunto de tarefas com custo (Story Points) e valor (ROI), encontrar a combinação que maximiza o valor entregue sem ultrapassar a capacidade da Sprint (40 SP).

Cada exercício aborda uma abordagem diferente — e revela um problema novo:

| Exercício | Abordagem        | Complexidade | Garante ótimo?                         |
| --------- | ---------------- | ------------ | -------------------------------------- |
| Ex 1      | Brute Force      | O(2ⁿ)        | Sim, mas inviável para n > 25          |
| Ex 2      | Greedy           | O(n log n)   | Não — pode ficar sub-ótimo             |
| Ex 3      | Análise empírica | —            | Mede a explosão exponencial na prática |
| Ex 4      | Hill Climbing    | O(n²)·iter   | Não — fica preso em mínimos locais     |

## Estrutura dos arquivos

```
exercicios_aula1.py     # arquivo principal — roda todos os exercícios
dados.py                # dados compartilhados (tarefas, capacidade, helpers)
ex1_brute_force.py      # exercício 1: busca exaustiva
ex2_greedy.py           # exercício 2: heurística gulosa
ex3_complexidade.py     # exercício 3: análise empírica de complexidade
ex4_hill_climbing.py    # exercício 4: hill climbing com restarts
```

## Como rodar

**Todos os exercícios de uma vez:**

```bash
python3 exercicios_aula1.py
```

**Cada exercício separado:**

```bash
python3 ex1_brute_force.py
python3 ex2_greedy.py
python3 ex3_complexidade.py
python3 ex4_hill_climbing.py
```

Não há dependências externas — só a biblioteca padrão do Python 3.

## Tarefas do problema

| ID  | Tarefa              | Custo (SP) | Valor ROI | ROI ratio |
| --- | ------------------- | ---------- | --------- | --------- |
| 0   | Auth OAuth2         | 8          | 40        | 5.00      |
| 1   | Dashboard métricas  | 13         | 55        | 4.23      |
| 2   | Exportar CSV        | 5          | 20        | 4.00      |
| 3   | Refactor serviço X  | 20         | 35        | 1.75      |
| 4   | API notificações    | 10         | 60        | 6.00      |
| 5   | Upgrade deps        | 3          | 15        | 5.00      |
| 6   | Testes E2E checkout | 8          | 50        | 6.25      |
| 7   | Rate limiting       | 6          | 45        | 7.50      |
| 8   | Docs OpenAPI        | 4          | 25        | 6.25      |
| 9   | Cache Redis         | 12         | 70        | 5.83      |

**Capacidade da Sprint:** 40 Story Points

## Resultado esperado

```
Abordagem             Valor       Tempo
-----------------------------------------
Brute Force             250      ~0.6ms
Greedy                  250     ~0.004ms
Hill Climbing           250      ~0.01ms
HC + Restarts           250      ~0.12ms
```

Ótimo global = **250 ROI** com as tarefas: API notificações + Testes E2E + Rate limiting + Docs OpenAPI + Cache Redis (40 SP exatos).

## Principais aprendizados

- **Brute Force** garante o ótimo mas escala exponencialmente — cada +2 tarefas quadruplica o tempo (razão ~4x, confirmando O(2ⁿ))
- **Greedy** é muito mais rápido, mas uma escolha localmente ótima pode bloquear combinações globalmente melhores
- **Hill Climbing** melhora o greedy explorando vizinhos, mas ainda fica preso em mínimos locais — rodar com partidas aleatórias diferentes gera resultados diferentes
- Nenhuma das três abordagens resolve bem o problema em escala → motivação para a próxima aula: **algoritmos bioinspirados**
