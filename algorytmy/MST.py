from typing import List, Dict, Tuple
import sys

Vertex = int
Graph = Dict[Vertex, List[Vertex]]
AdjMatr = List[List[int]]
Edge = Dict[Vertex, Vertex]
INF = sys.maxsize

def dpa(G: Graph, a: AdjMatr, s: Vertex) -> Tuple[List[Edge], int]:
    suma: int = 0
    A: List[Edge] = []
    V: List[Vertex] = [u for u in G.keys()]
    alfa: List[Vertex] = [0 for u in V]  # poprzednik wierzchołka
    beta: List[int] = [INF for u in V]   # waga krawędzi łączącej z MST
      #w grafie nieskierowanym reprezentowanym za pomocą listy sąsiedztwa każdy wierzchołek grafu musi znajdować się w zbiorze kluczy grafu
    Q: List[Vertex] = V  # wierzchołki nienależące do MST
    beta[s - 1] = 0
    Q.remove(s)
    u_gwiazdka: Vertex = s
    while Q:
        for u in Q:
            if u in G[u_gwiazdka]:
                if a[u - 1][u_gwiazdka - 1] < beta[u - 1]: #indeksy w macierzy wag są mniejsze o 1 od numeru wierzchołka
                    alfa[u - 1] = u_gwiazdka
                    beta[u - 1] = a[u - 1][u_gwiazdka - 1]
        u_gwiazdka = Q[0]    #nadanie u_gwiazdka przykładowej wartości
        for u in Q:
            if beta[u_gwiazdka - 1] > beta[u - 1]:   #szukanie takiego u_gwiazdka, dla którego waga krawędzi łączącej z MST jest najmniejsza
                u_gwiazdka = u
        Q.remove(u_gwiazdka)   #u_gwiazdka zapiszemy w  MST
        A.append({alfa[u_gwiazdka - 1]: u_gwiazdka})  #dodanie krawędzi do MST
        suma += a[alfa[u_gwiazdka - 1] - 1][u_gwiazdka - 1]  #zaktualizowanie sumy wag krawędzi drzewa
    return A, suma


G = {1: [(2, 2), (9, 2)],
            2: [(1, 2), (3, 3)],
            3: [(2, 3), (7, -4)],
            4: [(5, 4)],
            5: [(4, 4), (6, -6), (10, 7)],
            6: [(5, -6)],
            7: [(3, -4), (8, 1)],
            8: [(7, 1)],
            9: [(1, 2), (10, -1)],
            10: [(5, 7), (9, -1)]}
a: AdjMatr = [[INF for i in range(len(G))] for i in range(len(G))]
for k in G.keys():
    for v in G[k]:
        a[k - 1][v[0] - 1] = v[1]

g: Graph = {}
for k in G.keys():
    g[k] = []
    for v in G[k]:
        g[k].append(v[0])

print(a)

odp = dpa(g, a, 1)
print("MST to: {}, a suma wag to: {}".format(odp[0], odp[1]))





