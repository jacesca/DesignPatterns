# -*- coding: utf-8 -*-
"""
Provides some examples related to the iterator design pattern.
"""
################################################
# Iterator
# ----------------------------------------------
# A behavioral design pattern that lets you traverse elements of a
# collection without exposing its underlying representation
# (list, stack, tree, etc.).
# An object that facilitates the traversal of a data structure.
# ----------------------------------------------
# Motivation:
# How traversal of data structures happens and who makes it happen.
# Iteration (traversal) is a core functionality of various data structures.
# An iterator is a class that facilitates the traversal:
# - Keeps a reference to the current element.
# - Knows how to move to a different element.
# The iterator protocol requires:
# - __iter__() to expose the iterator, which uses
# - __next__() to return each of the iterated elements or
# - raise StopIteration when it's done
# ----------------------------------------------
# Summary:
# An iterator specified how you can traverse an object.
# Stateful iterators cannot be recursive.
# yield allows for much more succint iteration.
################################################

# Allow references to objects not created yet. E.g. left: Node=None
from __future__ import annotations


class Node:
    """An example class to create Nodes."""
    def __init__(self, value:int, left:Node=None, right:Node=None) -> None:
        self.value = value
        self.left = left
        self.right = right

        self.parent = None
        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __str__(self) -> str:
        left = self.left.value if self.left else None
        right = self.right.value if self.right else None
        return f'Node: {self.value} (Left: {left}, Right: {right})'
      
    def __repr__(self) -> str:
        left = self.left.value if self.left else None
        right = self.right.value if self.right else None
        return f'N: {self.value} (L: {left}, R: {right})'

    def __iter__(self) -> InOrderIterator:
        return InOrderIterator(self)


class InOrderIterator:
    "An example class to provide sequence to the Node clase."
    def __init__(self, root) -> None:
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self) -> Node:
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current

        # else:
        parent = self.current.parent
        while parent and self.current == parent.right:
            self.current = parent
            parent = parent.parent
        self.current = parent
        if self.current:
            return self.current

        # else:
        raise StopIteration


def traverse_in_order(root:Node) -> Node:
  def traverse(current:Node) -> Node:
    if current.left:
      for left in traverse(current.left):
        yield left
    yield current
    if current.right: 
      for right in traverse(current.right):
        yield right
  for node in traverse(root):
    yield node

if __name__ == '__main__':
    print('----------------------------------------------------------------------')
    print('Iterator pattern:')
    print('----------------------------------------------------------------------')
    print("""
    # The problem:
    #   1
    #  / \\
    # 2   3
    #
    # in order: 213
    # preorder: 123
    # postorder: 231        
    """)
    print('----------------------------------------------------------------------')
    root_node = Node(1, Node(2), Node(3))
    print(root_node)
    
    print('Iterating the node:')

    # Iteration form 1
    iter_node = iter(root_node)
    print([next(iter_node).value for cc in range(3)])

    # Iteration form 2
    print([item.value for item in root_node])
    # print([item for item in root_node])
    
    # Iteration form 3
    print([item.value for item in traverse_in_order(root_node)])

    #print([item for item in list(iter(root_node))])
    print('----------------------------------------------------------------------')
  