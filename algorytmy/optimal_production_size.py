from typing import List, Tuple, Optional, Union
import sys

INF = sys.maxsize


def optimal_production_size(min_capacity: int, max_capacity: int, production_need: List[int], productivity: int, production_cost: List[int], storage_cost: List[int], start_state: int, stop_state: int) -> Tuple[List[List[Tuple[Optional[int], Optional[int]]]], List[int], int]:
    '''
    Realizacja rozwiązania problemu wyznaczenia optymalnej wielkości partii produkcyjnej
    :param min_capacity: minimalna pojemność magazynu
    :param max_capacity: maksymalna pojemność magazynu
    :param production_need: miesięczne zapotrzebowanie na dany towar - lista wartości zapotrzeboania w kolejnych miesiąch
    :param productivity: zdolność produkcyjna zakładu
    :param production_cost: lista kosztów produkcji określonej ilości towaru (pierwsza wartość w liście - koszt produkcji
    0 towarów, kolejne wartości - koszt produkcji +1 towaru)
    :param storage_cost: koszt magazynowania określonej ilości towarów (pierwsza wartość - koszt magazynowania minimalnej
    liczby towarów (określona przez min_capacity), kolejne wartości - koszt magazynowania +1 towaru)
    :param start_state: startowa ilość towaru w magazynie
    :param stop_state: końcowa ilość towaru w magazynie
    :return: macierz decyzji, strategia i ostateczny koszt
    '''

    n: int = len(production_need)  # liczba rozpatrywanych miesięcy
    decision_matrix: List[List[Tuple[Optional[int], Optional[int]]]] = [[(None, None) for i in range(n)] for j in range(min_capacity, max_capacity + 1)]
    # macierz decyzji: wiersze - stan, kolumny - dany miesiąc, elementy tabeli - krotki, pierwszy element to podjęta decyzja, a drugi - wartość funkcji celu
    step: int = 0  # numer etapu(etapy numerowane od końca: 0 - ostatni etap)
    state_number: int = len(decision_matrix)  # liczba stanów
    for month in range(n)[::-1]:
        if step == 0:  # w ostatnim etapie musimy "trafić" w stan końcowy magazynu
            for state in range(state_number):  # przejrzenie stanów dla danego etapu
                elem_number = stop_state + production_need[month] - (state + min_capacity)  # najsilniejszym warunkiem w ostatnim etapie jest trafiene w stan końcowy, pozostałe są w nim zawarte (poza ograniczeniem z productivity)
                if elem_number < 0 or elem_number > productivity:  # nie możemy wyprodukować ujemnej lub większej od productivity ilości elementów, jest to stan zakazany
                    decision_matrix[state][step] = (None, INF)  # dla stanu zakazanego oznaczam liczbę wyprodukowanych elementów przez None, a koszt przez bardzo dużą liczbę (INF)
                else:
                    decision_matrix[state][step] = (elem_number, production_cost[elem_number] + storage_cost[stop_state - min_capacity])
                    # aktualizajca macierzy decyzji: ilość produkowanych elementów i koszt ich produkcji i przechowywania elementów, które muszą na końcu zostać w magazynie
        elif step < n - 1:  # dla etapów pośrednich musimy zminimalizować funkcję kosztu
            for state in range(state_number):
                min_decision = max(0, min_capacity + production_need[month] - (state + min_capacity))  # sprawdzam ograniczenia dla decyzji dla danego etapu i stanu - minimalna decyzja
                max_decision = min(productivity, max_capacity + production_need[month] - state - min_capacity)  # sprawdzenie ograniczeń - maksymalna decyzja
                poss_decision_costs = [production_cost[i] + storage_cost[state + i - production_need[month]] + decision_matrix[state + i - production_need[month]][step - 1][1] for i in range(min_decision, max_decision + 1)]
                # koszty możliwych decyzji dla danego stanu i etapu
                decision_cost = min(poss_decision_costs)  # podjęta decyzja to ta o minimalnym koszcie
                decision = poss_decision_costs.index(decision_cost) + min_decision  # znalezienie podjętej decyzji (indeks minimum kosztu + minimalna możliwa wartość decyzji)
                decision_matrix[state][step] = (decision, decision_cost)  # aktualizacja macierzy decyzji
        else:  # w pierwszym etapie rozważamy opcje tylko dla stanu początkowego:
            state = start_state - min_capacity  # w pierwszym etapie mamy jeden stan - stan startowy
            min_decision = max(0, min_capacity + production_need[month] - (state + min_capacity))  # sprawdzam ograniczenia dla decyzji dla danego etapu i stanu - minimalna decyzja
            max_decision = min(productivity, max_capacity + production_need[month] - state - min_capacity)  # sprawdzenie ograniczeń - maksymalna decyzja
            poss_decision_costs = [production_cost[i] + storage_cost[state + i - production_need[month]] + decision_matrix[state + i - production_need[month]][step - 1][1] for i in range(min_decision, max_decision + 1)]
            # koszty możliwych decyzji dla danego stanu i etapu
            decision_cost = min(poss_decision_costs)  # podjęta decyzja to ta o minimalnym koszcie
            decision = poss_decision_costs.index(decision_cost) + min_decision  # znalezienie podjętej decyzji (indeks minimum kosztu + minimalna możliwa wartość decyzji)
            decision_matrix[state][step] = (decision, decision_cost)  # aktualizacja macierzy decyzji
        step += 1
    # Wyznaczenie strategii:
    fin_cost = decision_matrix[start_state - min_capacity][-1][1]  # wyznaczenie ostetecznego kosztu
    strategy: List[int] = []  # strategia
    decision_state = start_state - min_capacity  # stan, dla którego decyzja zostanie umieszczona w strategii
    for st in range(n)[::-1]:  # odtworzenie strategii na podtsawie decyzji dla etapów
        strategy.append(decision_matrix[decision_state][st][0])
        decision_state = decision_state + decision_matrix[decision_state][st][0] - production_need[-st - 1]
    return decision_matrix, strategy, fin_cost


def print_decision_matrix(matrix: List[List[Tuple[int, int]]], Ymin: int):
    n = len(matrix)
    print("y_i-1  ", end='')
    for i in range(len(matrix[0])):
        print(f" x{n - i:^2d}|f{i + 1:^2d}(y{n - i - 1})", end='')
        if i != n - 1:
            print("  ", end='')
    print()
    for i in range(n):
        print(f"{(i + Ymin):^5d}  ", end='')
        for j in range(len(matrix[0])):
            choice: Optional[int, str] = matrix[i][j][0]
            if choice is None:
                print(" - ", end=' ')
            else:
                print(f"{choice:^3d}", end=' ')
            value: Union[int, float] = matrix[i][j][1]
            if value is None:
                print("  -   ", end=' ')
            elif value >= INF:
                print("  inf  ", end='')
            else:
                print(f"{value:^7d}", end='')
            print("   ", end='')
        print()


if __name__ == '__main__':
    min_cap = 1
    max_cap = 5
    prod_need = [4, 5, 3, 1, 3, 2, 6, 5, 2, 0, 3, 4]
    prod = 6
    prod_cost = [2, 7, 12, 16, 19, 21, 22]
    stor_cost = [2, 3, 3, 4, 4]
    start_state = 2
    stop_state = 3
    dec, strat, f_c = optimal_production_size(min_cap, max_cap, prod_need, prod, prod_cost, stor_cost, start_state, stop_state)
    print("Macierz decyzji: ")
    print_decision_matrix(dec, 1)
    print("Strategia (ilość produkowanego towaru w koljenych mesiącach): ", strat)
    print("Ostateczny koszt: ", f_c)
