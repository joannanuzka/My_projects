from typing import List, Tuple, Optional
import sys

INF = sys.maxsize


def johnson2(task_matr: List[List[int]]) -> Tuple[List[int], List[List[int]], int]:
    optimal_order: List[List[Optional[int]]] = [[None for i in range(len(task_matr[0]))] for j in range(3)]
    # tablica, w której znajduje się optymalna kolejność zadań (pierwszy wiersz) i czas ich wykonania na pierwszej
    # i drugiej maszynie (drugi i trzeci wiersz)
    min1 = min(task_matr[0])  # minimum w pierwszym wierszu
    min2 = min(task_matr[1])  # minimum w drugim wierszu
    start_indx = 0  # indeks pierwszego wolnego elementu
    end_indx = len(task_matr[0]) - 1  # indeks ostatniego wolnego elementu
    while min1 != INF:
        if min1 < min2:
            index_min = task_matr[0].index(min1)
            optimal_order[0][start_indx] = index_min + 1  # dodanie na pierwszym wolnym miejscu numeru zadania
            # (zadania numerowane od 1, indeksy w liście od 0, dlatego indeks trzeba zwiekszyć)
            optimal_order[1][start_indx] = min1  # dodanie czasu wykonywania zadania przez pierwszą maszynę
            optimal_order[2][start_indx] = task_matr[1][index_min]  # dodanie czasu wykonywania zadania przez drugą maszynę
            start_indx += 1  # aktualizacja indeksu pierwszego wolnego miejsca
            task_matr[0][index_min] = INF
            task_matr[1][index_min] = INF  # wykreślenie kolumny
        elif min2 < min1:
            index_min = task_matr[1].index(min2)
            optimal_order[0][end_indx] = index_min + 1  # dodanie na ostatnim wolnym miejscu numeru zadania
            optimal_order[1][end_indx] = task_matr[0][index_min]  # dodanie czasu wykonywania zadania przez pierwszą maszynę
            optimal_order[2][end_indx] = min2  # dodanie czasu wykonywania zadania przez drugą maszynę
            end_indx -= 1  # aktualizacja indeksu ostatniego wolnego miejsca
            task_matr[0][index_min] = INF
            task_matr[1][index_min] = INF  # wykreślenie kolumny
        else:
            index_min1 = task_matr[0].index(min1)
            index_min2 = task_matr[1].index(min2)
            if index_min1 == index_min2:  # jeżeli znalezione minimalne czasy dotyczą tego samego zadania
                # zadanie na pierwsze wolne miejsce
                optimal_order[0][start_indx] = index_min1 + 1  # dodanie na pierwszym wolnym miejscu numeru zadania
                # (zadania numerowane od 1, indeksy w liście od 0, dlatego indeks trzeba zwiekszyć)
                optimal_order[1][start_indx] = min1  # dodanie czasu wykonywania zadania przez pierwszą maszynę
                optimal_order[2][start_indx] = min2  # dodanie czasu wykonywania zadania przez drugą maszynę
                start_indx += 1  # aktualizacja indeksu pierwszego wolnego miejsca
                task_matr[0][index_min1] = INF
                task_matr[1][index_min1] = INF  # wykreślenie kolumny
            else:  # w przeciwnym wypadku dodaję jedno zadanie na początek i drugie na koniec
                optimal_order[0][start_indx] = index_min1 + 1  # dodanie na pierwszym wolnym miejscu numeru zadania
                # (zadania numerowane od 1, indeksy w liście od 0, dlatego indeks trzeba zwiekszyć)
                optimal_order[1][start_indx] = min1  # dodanie czasu wykonywania zadania przez pierwszą maszynę
                optimal_order[2][start_indx] = task_matr[1][index_min1]  # dodanie czasu wykonywania zadania przez drugą maszynę
                start_indx += 1  # aktualizacja indeksu pierwszego wolnego miejsca
                task_matr[0][index_min1] = INF
                task_matr[1][index_min1] = INF  # wykreślenie kolumny
                optimal_order[0][end_indx] = index_min2 + 1  # dodanie na ostatnim wolnym miejscu numeru zadania
                optimal_order[1][end_indx] = task_matr[0][
                    index_min2]  # dodanie czasu wykonywania zadania przez pierwszą maszynę
                optimal_order[2][end_indx] = min2  # dodanie czasu wykonywania zadania przez drugą maszynę
                end_indx -= 1  # aktualizacja indeksu ostatniego wolnego miejsca
                task_matr[0][index_min2] = INF
                task_matr[1][index_min2] = INF  # wykreślenie kolumny
        min1 = min(task_matr[0])  # nowe minimum w pierwszym wierszu
        min2 = min(task_matr[1])  # nowe minimum w drugim wierszu
    task_order: List[int] = [optimal_order[0][0]]  # lista kolejnych wykonywanych zadań
    time: List[List[int]] = [[optimal_order[1][0]], [optimal_order[1][0] + optimal_order[2][0]]]
    # czas zakończenia wykonywania zadań
    for indx in range(1, len(optimal_order[0])):
        task_order.append(optimal_order[0][indx])
        time[0].append(time[0][indx - 1] + optimal_order[1][indx])  # czasy zakończenia zadań przez pierwszą maszynę
        time[1].append(max(time[0][indx], time[1][indx - 1]) + optimal_order[2][indx])  # czasy zakończenia zadań przez drugą maszynę
    final_time = time[1][len(time[0]) - 1]  # ostateczny czas zakończenia zadań
    return task_order, time, final_time


def johnson3(task_matr: List[List[int]]) -> Tuple[List[int], List[List[int]], int]:
    min1 = min(task_matr[0])
    max2 = max(task_matr[1])
    min3 = min(task_matr[2])
    if min1 >= max2 or min3 >= max2:  # sprawdzenie warunku, czy możemy sprowadzić problem do zagadnienia dwumaszynowego
        t12: List[int] = []
        t23: List[int] = []
        for i in range(len(task_matr[0])):
            t12.append(task_matr[0][i] + task_matr[1][i])
            t23.append(task_matr[1][i] + task_matr[2][i])  # utworzenie pomocniczych dwóch maszyn
        order_two_m, _, _ = johnson2([t12, t23])  # uszeregowanie wykonywania zadań na podstawie alg. dla dwóch maszyn
        task_time: List[List[int]] = [[], [], []]  # czas wykonywania zadań na każdej z trzech maszyn - zadania są uszeregowane
        for task in order_two_m:
            task_time[0].append(task_matr[0][task - 1])
            task_time[1].append(task_matr[1][task - 1])
            task_time[2].append(task_matr[2][task - 1])
        final_time: List[List[int]] = [[task_time[0][0]], [task_time[0][0] + task_time[1][0]],[task_time[0][0] + task_time[1][0] + task_time[2][0]]]   # czasy zakończenia działań na każdej z maszyn
        for indx in range(1, len(task_time[0])):
            final_time[0].append(final_time[0][indx - 1] + task_time[0][indx])
            final_time[1].append(max(final_time[0][indx], final_time[1][indx - 1]) + task_time[1][indx])
            final_time[2].append(max(final_time[1][indx], final_time[2][indx - 1]) + task_time[2][indx])
        all_tasks_fin = final_time[2][-1]  # ostateczny czas zakończenia wszystkich działań
        return order_two_m, final_time, all_tasks_fin
    else:
        print("Niemożliwe rozwiązanie za pomocą algorytmu Johnsona dla dwóch maszyn")
        return None, None, None


def print_tasks(task_list, time_matr):
    print("Z    [", end='')
    for elem in task_list:
        print(f"{elem:4d}", end='')
    print("]\n")
    for i in range(len(time_matr)):
        print("M", i + 1, " [", end='')
        for elem in time_matr[i]:
            print(f"{elem:4d}", end='')
        print("]\n")


if __name__ == '__main__':
    matrix = [[7, 8, 12, 11, 8, 6, 10, 9, 9, 7],
              [2, 3, 5, 4, 1, 2, 5, 6, 3, 2],
              [4, 6, 8, 10, 9, 7, 6, 8, 5, 12]]
    tasks = [i for i in range(1, 11)]
    order, tasks_fin_time, final_time = johnson3(matrix)
    print("Uszeregowanie zadań: ")
    print(order)
    print("Czas zakończenia wykonywania zadań na poszczególnych maszynach:")
    print_tasks(order, tasks_fin_time)
    print("Czas zakończenia działań: ", final_time)
    print("\n")
    print_tasks(tasks, matrix)
