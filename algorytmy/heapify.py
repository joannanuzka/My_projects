from __future__ import annotations
from typing import Any, List

import random
from timeit import default_timer as timer


class Elem:
    data: Any
    priority: int

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        return "{" + str(self.data) + ":" + str(self.priority) + "}"


class PriorityQueue:
    tab: List[Elem]

    def __init__(self):
        self.tab = []

    def is_empty(self):
        return not self.tab

    def peek(self):
        return self.tab[0] if self.tab else None

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            val = self.tab[0]
            self.tab[0] = self.tab[-1]
            self.tab.pop()
            for i in range(len(self.tab) // 2):
                if 2 * i + 1 < len(self.tab) and self.tab[i] < self.tab[2 * i + 1]:
                    temp = self.tab[i]
                    self.tab[i] = self.tab[2 * i + 1]
                    self.tab[2 * i + 1] = temp
                if 2 * i + 2 < len(self.tab) and self.tab[i] < self.tab[2 * i + 2]:
                    temp2 = self.tab[i]
                    self.tab[i] = self.tab[2 * i + 2]
                    self.tab[2 * i + 2] = temp2
            return val

    def enqueue(self, data, priority):
        self.tab.append(Elem(data, priority))
        i = len(self.tab) - 1
        while i > 0:
            if self.tab[i] > self.tab[(i - 1) // 2]:
                temp = self.tab[i]
                self.tab[i] = self.tab[(i - 1) // 2]
                self.tab[(i - 1) // 2] = temp
            i -= 1

    def print_tab(self):
        string = "[ "
        for i in range(len(self.tab)):
            string += str(self.tab[i]) + " "
        string += "]"
        print(string)

    def print_tree(self):
        print("==============")
        self._print_tree(0, 0)
        print("==============")

    def _print_tree(self, lvl, indx):
        if indx < len(self.tab):
            self._print_tree(lvl + 10, 2 * indx + 2)
            print()
            for i in range(10, lvl + 10):
                print(end=" ")
            print(self.tab[indx])
            self._print_tree(lvl + 10, 2 * indx + 1)

    def heapify(self, tab_prio: List[int]):
        for elem in tab_prio:
            self.tab.append(Elem("A", elem))
        if len(tab_prio) < 100:
            print("Tablica oryginalna: ")
            self.print_tab()
            print("Drzewo: ")
            self.print_tree()
        leaf_number = (len(self.tab) + 1) // 2
        not_leaf = (len(self.tab)) - leaf_number
        i = not_leaf
        while i >= 0:
            j = i
            while 2 * j + 1 < len(self.tab):
                if self.tab[j] < self.tab[2 * j + 1] or (
                        2 * j + 2 < len(self.tab) and self.tab[j] < self.tab[2 * j + 2]):
                    if 2 * j + 2 < len(self.tab) and self.tab[2 * j + 2] > self.tab[2 * j + 1]:
                        temp = self.tab[j]
                        self.tab[j] = self.tab[2 * j + 2]
                        self.tab[2 * j + 2] = temp
                        j = 2 * j + 2
                    else:
                        temp = self.tab[j]
                        self.tab[j] = self.tab[2 * j + 1]
                        self.tab[2 * j + 1] = temp
                        j = 2 * j + 1
                else:
                    break
            i -= 1


if __name__ == '__main__':
    tab1 = [3, 6, 1, 8, 4, 12, 7, 13, 9, 22, 15, 5, 11, 16, 18, 20, 25, 21, 27, 30]
    heap1 = PriorityQueue()
    heap1.heapify(tab1)
    print("Kopiec:")
    heap1.print_tab()
    heap1.print_tree()
    tab_sort = [None for i in range(len(tab1))]
    for indx in range(len(tab_sort)):
        tab_sort[-indx - 1] = heap1.dequeue().priority
    print("Posortowana tablica: ", tab_sort)

    tab2 = []
    for i in range(10000):
        tab2.append(random.randint(0, 1000))

    start1 = timer()
    heap2 = PriorityQueue()
    heap2.heapify(tab2)
    tab_sort2 = [None for i in range(len(tab2))]
    for indx in range(len(tab_sort2)):
        tab_sort2[-indx - 1] = heap2.dequeue().priority
    end1 = timer()
    print("Czas heapify: ", end1 - start1)

    start2 = timer()
    heap3 = PriorityQueue()
    for elem in tab2:
        heap3.enqueue("A", elem)
    tab_sort3 = [None for i in range(len(tab2))]
    for indx in range(len(tab_sort3)):
        tab_sort3[-indx - 1] = heap3.dequeue().priority
    end2 = timer()
    print("Czas enqueue: ", end2 - start2)








