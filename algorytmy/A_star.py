from typing import List, Dict, Tuple

def h1(G, start, koniec, min_w):  # graf w formie listy sąsiedztwa z wagami
    h = G[start][0][1] + min_w # początkowa przewidywana wartość heurystyki to odległość między startem,
        # a pierwszym wierzchołkiem w liście sąsiadów startu powiększona o minimalną wartość krawędzi w grafie
    for v in G[start]:
        if v[0] == koniec:  #czy koniec jest sąsiadem startu:
            if h >= v[1]:    #czy odległość między startem a końcem jest na pewno minimalna
                h = v[1]
        else:
            if v[1] + min_w < h: #czy z któregoś wierzchołka możemy dojść szybciej
                h = v[1] + min_w
    return h


def get_first(lst: List[Tuple[int, int]]): # funkcja zwaracająca pierwszą wartość kolejki priorytetowej
    first = lst[0]
    index = 0
    for indx in range(len(lst)):
        if lst[indx][1] < first[1]:  # druga wartość w krotce to waga
            first = lst[indx]
            index = indx
    del lst[index]
    return first


def A_star_temp(G, start, koniec, h):  # h - stosowana funkcja h(x, y)
    min_w = G[start][0][1]  # min_w - minimalna waga występująca w grafie
    for key in G:
        for v in G[key]:
            if v[1] < min_w:
                min_w = v[1]
    Q : List[Tuple[int, int]] = []  # kolejka priorytetytowa
    Q.append((start, h(G, start, koniec, min_w)))
    C: List[int] = [] # lista węzłów odwiedzonych
    M: Dict[int, Tuple[int, int]] = {} # słownik, w którym węzłowi przyporządkowany jest jego rodzic i odległość od startu
    M[start] = (None, 0)
    while Q:  # kiedy kolejka nie jest pusta
        u = get_first(Q)[0]  # pobierz pierwszy element kolejki
        if u == koniec:
            break
        C.append(u) # dodanie wierzchołka do odwiedzonych
        for v in G[u]:  # iteracja po sąsiadach u
            if v[0] in C: # jeśli wierzchołek jest odwiedzony pomijamy dalsze instrukcje i idziemy do kolejnego
                continue
            u_dist = M[u][1] # odległość u od startu
            tmp_dist = u_dist + v[1] # tymczasowa odległość v od startu
            v_in_Q = False
            for elem in Q:
                if elem[0] == v[0]:
                    v_in_Q = True
            if not v_in_Q:  # jeśli kolejka nie zawiera v
                Q.append((v[0], tmp_dist + h(G, v[0], koniec, min_w)))
                M[v[0]] = (u, tmp_dist)  #dodajemy węzeł do słownika i kolejki
            else:
                v_dist = M[v[0]][1] #jeśli v jest w kolejce, pobieramy jego odległość od startu
                if tmp_dist < v_dist: # jeśli znaleźliśmy krótszą drogę do v - aktualizacja
                    M[v[0]] = (u, tmp_dist)
                    for indx in range(len(Q)):
                        if Q[indx][0] == v[0]:
                            Q[indx] = (v[0], tmp_dist + h(G, v[0], koniec, min_w))
                            break
    return M

def A_star(G, start, koniec, h): # zwrócenie wyniku funkcji w postaci czytelniejszej dla człowieka:
    M = A_star_temp(G, start, koniec, h)
    odl = M[koniec][1]
    prev = M[koniec][0]
    lst = [koniec]
    lst_sort = []
    while prev:
        lst.append(prev)
        prev = M[prev][0]
    for i in range(len(lst)):
        lst_sort.append(lst[- i - 1])
    return lst_sort, odl


G = {1: [(2, 7), (8, -2)],
            2: [(1, 7), (3, 3), (4, 7)],
            3: [(2, 3), (9, 5)],
            4: [(2, 7), (10, 6)],
            5: [(8, 6)],
            6: [(8, -1)],
            7: [(10, 2)],
            8: [(1, -2), (5, 6), (6, -1)],
            9: [(3, 5)],
            10: [(4, 6), (7, 2)]}

print(A_star(G, 1, 10, h1))





