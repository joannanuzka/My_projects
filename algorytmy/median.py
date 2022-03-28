import random


def find_median(lst, start, stop):
    n = (start + stop)//2
    m = (len(lst) - 1)//2
    elem = lst[n]
    i = start
    j = stop
    while i < j:
        while lst[i] < elem:
            if i == j:
                break
            i += 1
        while lst[j] > elem:
            if j == i:
                break
            j -= 1
        if i < j:
            lst[i], lst[j] = (lst[j], lst[i])
            i += 1
            j -= 1
    if i == m or j == m:
        return lst[m]
    elif i < len(lst)//2:
        return find_median(lst, i, stop)
    else:
        return find_median(lst, start, i)


def quicksort(lst, start=0, stop=None, it_number=0):
    if stop is None:
        stop = len(lst) - 1
    median_list = []
    first_indx = start
    while first_indx < stop:
        end_indx = first_indx + 4 if first_indx + 4 < stop else stop
        median_list.append(find_median(lst[first_indx: end_indx + 1], 0, end_indx - first_indx))
        first_indx += 5
    pivot = find_median(median_list, 0, len(median_list) - 1)
    i = start
    j = stop
    if it_number < 3:
        print("Aktualna lista: ", lst[start: stop + 1])
        print("Element ją dzielący: ", pivot)
    while i < j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = (lst[j], lst[i])
            i += 1
            j -= 1
    if start < j:
        quicksort(lst, start, j, it_number + 1)
    if stop > i:
        quicksort(lst, i, stop, it_number + 1)


if __name__ == '__main__':
    tab = []
    for i in range(64):
        tab.append(random.randint(0, 100))
    print("Lista początkowa: ")
    print(tab)
    quicksort(tab)
    print("Lista posortowana: ")
    print(tab)
