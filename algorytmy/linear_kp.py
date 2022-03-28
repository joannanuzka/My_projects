from typing import List, Tuple, Optional


def linear_kp(weights: List[int], d: List[int], profits: List[int], max_weight: int) -> Tuple[
    List[List[Tuple[Optional[int], Optional[int]]]], List[int], int]:
    """
    Funkcja realizująca problem liniowego zagadnienia załadunku
    :param weights: lista wag elementów (id elementu to jego indeks)
    :param d: lista zawierające informacje o dostępności elementów (id elementu to jego indeks)
    :param profits: lista zawierająca współczynniki liniowej funkcji zysku dla każdego z elelmentów, funkcja jest postaci: f(el) = c * el, gdzie c to odpowiednia wartość współczynnika umieszczona w liście, a el - lczba zabieranych elementów
    :param max_weight: maksymalna dopuszczalna waga wszystkich zabieranych elementów
    :return:
    """

    n = len(weights)  # liczba rodzajów elementów
    decision_matrix: List[List[Tuple[Optional[int], Optional[int]]]] = [[(None, None) for step in range(n)] for state in
                                                                        range(
                                                                            max_weight + 1)]  # macierz decyzji dla każdego etapu (kolumny macierzy) i stanu (wiersze), elementami macierzy są dwuelementowe krotki, w których pierwszy element zawiera informację o ilości zabranych przedmiotów, a drugi - wartość funkcji zysku
    step = 0  # numer etapu
    state_number = len(decision_matrix)  # ilość stanów
    for elem_id in range(n)[::-1]:
        if step == 0:  # w ostatnim etapie zabieramy maksymalną możliwą ilość przedmiotów
            for state in range(state_number):
                elem_number = min(state // weights[elem_id],
                                  d[elem_id])  # ilość zabieranych elementów dla każdego stanu
                decision_matrix[state][step] = (
                    elem_number, elem_number * profits[elem_id])  # aktualizacja macierzy decyzji
        elif step < n - 1:  # dla etapów pośrednich musimy zmaksymalizować funkcję zysku dla każdego stanu
            for state in range(state_number):
                poss_list = [
                    profits[elem_id] * elem_number + decision_matrix[state - elem_number * weights[elem_id]][step - 1][
                        1] for elem_number in range(min(state // weights[elem_id] + 1, d[
                        elem_id]))]  # lista zysków dla możliwych ilości wzięteych rzeczy
                decision_pr = max(poss_list)  # wybranie maksymalnego możliwego zysku
                dec_el_number = poss_list.index(decision_pr)
                decision_matrix[state][step] = (dec_el_number, decision_pr)  # aktualizacja macierzy decyzji
        else:
            state = max_weight  # w pierwszym etapie występuje tylko jeden stan: maksymalna waga zabieranych elementów
            poss_list = [
                profits[elem_id] * elem_number + decision_matrix[state - elem_number * weights[elem_id]][step - 1][1]
                for elem_number in range(min(state // weights[elem_id] + 1,
                                             d[elem_id]))]  # lista zysków dla możliwych ilości wzięteych rzeczy
            decision_pr = max(poss_list)  # wybranie maksymalnego możliwego zysku
            dec_el_number = poss_list.index(decision_pr)
            decision_matrix[state][step] = (dec_el_number, decision_pr)  # aktualizacja macierzy decyzji
        step += 1
    # Wyznaczenie strategii:
    profit = decision_matrix[-1][-1][1]  # ostateczny zysk
    decision_state = max_weight  # decyzja dla denego stanu
    strategy = []  # strategia
    for st in range(n)[::-1]:  # odtworzenie strategii na podtsawie decyzji dla etapów
        strategy.append(decision_matrix[decision_state][st][0])
        decision_state = decision_state - decision_matrix[decision_state][st][0] * weights[st]
    return decision_matrix, strategy, profit


def print_matr(matr):
    print("Stan   ", end='')
    for i in range(len(matr[0])):
        print("Z", i + 1, "    ", end='')
    j = 0
    print("")
    for lst in matr:
        print(j, "   ", lst)
        j += 1


if __name__ == '__main__':
    w = [2, 3, 5, 6, 3, 1, 4, 2, 7, 5]
    d = [5, 2, 4, 1, 5, 3, 7, 9, 3, 6]
    pr = [1, 4, 3, 7, 2, 1, 6, 3, 9, 4]
    m_w = 25
    d_m, strat, prof = linear_kp(w, d, pr, m_w)
    print_matr(d_m)
    print("\n")
    print("Element: ", [i for i in range(10)])
    print("Ilość:   ", strat)
    print("Zysk:", prof)
