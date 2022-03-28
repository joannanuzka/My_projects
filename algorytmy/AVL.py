from __future__ import annotations

from typing import Any, Optional


class Node:
    key: int
    val: Any
    left: Optional[Node]
    right: Optional[Node]
    balance_factor: int

    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0


class Root:
    head: Optional[Node]

    def __init__(self):
        self.head = None

    def search(self, k):
        node = self._search(k, self.head)
        return node.val

    def _search(self, k, node):
        if not node:
            print("Brak wartości o podanym kluczu")
            return None
        if k == node.key:
            return node
        if k > node.key:
            if node.right:
                return self._search(k, node.right)
            else:
                print("Brak wartości o podanym kluczu")
                return None
        else:
            if node.left:
                return self._search(k, node.left)
            else:
                print("Brak wartości o podanym kluczu")
                return None

    def insert(self, k, v):
        if not self.head:
            self.head = Node(k, v)
            return None
        else:
            self.head = self._insert(k, v, self.head)

    def _insert(self, k, v, node):
        if not node:
            return Node(k, v)
        if k > node.key:
            node.right = self._insert(k, v, node.right)
            return node
        elif k < node.key:
            node.left = self._insert(k, v, node.left)
            return node
        else:
            node.val = v
            return node

    def delete(self, k):
        self.head = self._delete(k, self.head)

    def _delete(self, k, node):
        if not node:
            print("Nie ma elementu o podanym kluczu, więc nie można go usunąć")
            return None
        if k > node.key:
            node.right = self._delete(k, node.right)
            return node
        elif k < node.key:
            node.left = self._delete(k, node.left)
            return node
        else:
            if not node.right and not node.left:
                return None
            elif not node.right and node.left:
                return node.left
            elif node.right and not node.left:
                return node.right
            else:
                n = node.right
                rodzic_n = node
                if not n.left:
                    n.left = node.left
                    return n
                else:
                    n = n.left
                    rodzic_n = rodzic_n.right
                while n.left:
                    n = n.left
                    rodzic_n = rodzic_n.left
                n.left = node.left
                rodzic_n.left = n.right
                n.right = node.right
                return n

    def print(self):
        if self.head:
            print("Wartości i klucze w drzewie:")
            self._print(self.head)

    def _print(self, node):
        if node.left:
            self._print(node.left)
        print(node.key, " - ", node.val)
        if node.right:
            self._print(node.right)

    def height(self, node=None):
        if not node:
            return self._height(self.head, 0)
        else:
            node = self._search(node, self.head)
            return self._height(node, 0)

    def _height(self, node, level):
        if node.right:
            lvl_right = self._height(node.right, level + 1)
        else:
            lvl_right = level
        if node.left:
            lvl_left = self._height(node.left, level + 1)
        else:
            lvl_left = level
        return max(lvl_left, lvl_right)

    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl+10)
            print()
            for i in range(10, lvl+10):
                print(end = " ")
            print(node.key)
            self._print_tree(node.left, lvl+10)


class AVL(Root):
    def __init__(self):
        super().__init__()

    def RR(self, node: Node):
        kid = node.right
        node.right = kid.left
        kid.left = node
        if kid.balance_factor == -1:
            node.balance_factor = 0
            kid.balance_factor = 0
        elif kid.balance_factor == 0:
            node.balance_factor = -1
            kid.balance_factor = 1
        return kid

    def LL(self, node: Node):
        kid = node.left
        node.left = kid.right
        kid.right = node
        if kid.balance_factor == 1:
            node.balance_factor = 0
            kid.balance_factor = 0
        elif kid.balance_factor == 0:
            node.balance_factor = 1
            kid.balance_factor = -1
        return kid

    def RL(self, node: Node):
        kid1 = node.right
        kid2 = kid1.left
        node.right = kid2.left
        kid1.left = kid2.right
        kid2.left = node
        kid2.right = kid1
        if kid2.balance_factor == -1:
            node.balance_factor = 1
            kid1.balance_factor = 0
            kid2.balance_factor = 0
        elif kid2.balance_factor == 0:
            node.balance_factor = 0
            kid1.balance_factor = 0
        elif kid2.balance_factor == 1:
            node.balance_factor = 0
            kid1.balance_factor = -1
            kid2.balance_factor = 0
        return kid2

    def LR(self, node: Node):
        kid1 = node.left
        kid2 = kid1.right
        node.left = kid2.right
        kid1.right = kid2.left
        kid2.right = node
        kid2.left = kid1
        if kid2.balance_factor == -1:
            node.balance_factor = 0
            kid1.balance_factor = 1
            kid2.balance_factor = 0
        elif kid2.balance_factor == 0:
            node.balance_factor = 0
            kid1.balance_factor = 0
        elif kid2.balance_factor == 1:
            node.balance_factor = -1
            kid1.balance_factor = 0
            kid2.balance_factor = 0
        return kid2

    def update_balance(self, node):
        if node.left:
            self.update_balance(node.left)
        if node.left and node.right:
            node.balance_factor = self._height(node.left, 0) - self._height(node.right, 0)
        elif node.left:
            node.balance_factor = self._height(node, 0)
        elif node.right:
            node.balance_factor = -self._height(node, 0)
        else:
            node.balance_factor = 0
        if node.right:
            self.update_balance(node.right)

    def balance_tree(self, node: Node):
        if node.left:
            node.left = self.balance_tree(node.left)
        if node.right:
            node.right = self.balance_tree(node.right)
        if node.balance_factor < -1:
            if node.right.balance_factor <= 0:
                return self.RR(node)
            else:
                return self.RL(node)
        elif node.balance_factor > 1:
            if node.left.balance_factor >= 0:
                return self.LL(node)
            else:
                return self.LR(node)
        else:
            return node

    def insert(self, k, v):
        if not self.head:
            self.head = Node(k, v)
        else:
            self.head = self._insert(k, v, self.head)
            self.update_balance(self.head)
            self.head = self.balance_tree(self.head)

    def delete(self, k):
        self.head = self._delete(k, self.head)
        self.update_balance(self.head)
        self.head = self.balance_tree(self.head)


if __name__ == '__main__':
    BST = AVL()
    BST.insert(50, "A")
    BST.insert(15, "B")
    BST.insert(62, "C")
    BST.insert(5, "D")
    BST.insert(2, "E")
    BST.insert(1, "F")
    BST.insert(11, "G")
    BST.insert(100, "H")
    BST.insert(7, "I")
    BST.insert(6, "J")
    BST.insert(55, "K")
    BST.insert(52, "L")
    BST.insert(51, "M")
    BST.insert(57, "N")
    BST.insert(8, "O")
    BST.insert(9, "P")
    BST.insert(10, "R")
    BST.insert(99, "S")
    BST.insert(12, "T")
    BST.print_tree()
    BST.print()
    print("Dana o kluczu 10 to ", BST.search(10))
    BST.delete(50)
    BST.delete(52)
    BST.delete(11)
    BST.delete(57)
    BST.delete(1)
    BST.delete(12)
    BST.insert(3, "AA")
    BST.insert(4, "BB")
    BST.delete(7)
    BST.delete(8)
    BST.print()
    BST.print_tree()




